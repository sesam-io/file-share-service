from flask import Flask, request, Response, send_from_directory
from datetime import datetime, timedelta
from urllib.parse import urljoin
import argparse
import json
import os
import sys

def datetime_format(dt_int):
    seconds = (dt_int//1000000000)
    nanoseconds = dt_int-(dt_int//1000000000)*1000000000
    nanoseconds_str = ("%09d" % nanoseconds).rstrip("0")
    dt = datetime.utcfromtimestamp(seconds)
    if len(nanoseconds_str) > 0:
        return '%04d' % dt.year + dt.strftime("-%m-%dT%H:%M:%S") + "." + nanoseconds_str + "Z"
    else:
        return '%04d' % dt.year + dt.strftime("-%m-%dT%H:%M:%SZ")

    
def to_transit_datetime(dt_int):
    return "~t" + datetime_format(dt_int)


class DataAccess:
    
    def __init__(self, directory, base_url):
        self.directory = directory
        self.base_url = base_url

    def get_entities(self, since):
        entities = list(self._get_file_entities())
        entities.sort(key=lambda x: x["_updated"])
        if since is None:
            return entities
        else:
            return [entity for entity in entities if entity["_updated"] > since]

    def _get_file_entities(self):
        for absfile in self._get_absfiles():
            entity = self._create_file_entity(absfile)
            if entity is not None:
                yield entity
                
    def _get_absfiles(self):
        for root, dirs, files in os.walk(self.directory):
            for d in dirs:
                yield os.path.join(root, d)
            for f in files:
                yield os.path.join(root, f)

    def _create_file_entity(self, absfile):
        relfile = os.path.relpath(absfile, start=self.directory)
        path = relfile.split(os.sep)
        # filter out files with parts starting with "." (hidden files)
        for p in path:
            if p.startswith("."):
                return

        url = "~r%s/%s" % (urljoin(self.base_url, "file"), relfile)
        r = os.stat(absfile)
        entity = {
            "_id": relfile,
            "_updated": datetime_format(r.st_mtime_ns),
            "file": os.path.basename(relfile),
            "dir": os.path.dirname(relfile),
            "path": path,
            "atime": to_transit_datetime(r.st_atime_ns),
            # "birthtime": r.st_birthtime,
            "ctime": to_transit_datetime(r.st_ctime_ns),
            "gid": r.st_gid,
            "mode": r.st_mode,
            "mtime": to_transit_datetime(r.st_mtime_ns),
            "size": r.st_size,
            "uid": r.st_uid,
        }

        if os.path.isfile(absfile):
            entity["url"] = url
            entity["type"] = "file"
        elif os.path.isdir(absfile):
            entity["type"] = "dir"
        elif os.path.islink(absfile):
            entity["type"] = "link"
        elif os.path.ismount(absfile):
            entity["type"] = "mount"
        else:
            entity["type"] = "unknown"

        return entity

    def get_absfile(self, relpath):
        return os.join(self.directory, relpath)


app = Flask(__name__)


@app.route('/files')
def get_entities():
    since = request.args.get('since')
    entities = data_access_layer.get_entities(since)
    return Response(json.dumps(entities), mimetype='application/json')

@app.route('/file/<path:filename>')
def get_file(filename):
    print("1", filename)
    directory = os.path.abspath(data_access_layer.directory)
    print("x", directory)
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/file2/<path:filename>')
def get_file2(filename):
    print(filename)
    absfile = data_access_layer.get_absfile(filename)
    print(absfile)
    return send_file(absfile)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Run the file-share service')
    
    parser.add_argument('-u', dest='base_url', required=True,
                        help='The base URL to refer back to the service')

    parser.add_argument('directory', nargs='?',
                        help='The directory to serve')
    args = parser.parse_args()

    directory = args.directory if args.directory else os.getcwd()
    if not os.path.exists(directory):
        print("Directory '%s' does not exists" % (directory,))
        sys.exit(1)
        
    print("Serving directory '%s'..." % (directory,))

    # create data access object
    data_access_layer = DataAccess(directory, args.base_url)

    # start web server
    app.run(debug=True, host='0.0.0.0')
