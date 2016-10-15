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
    
    def __init__(self, directory, args):
        self.directory = directory
        self.args = args

    def get_entities(self, request):
        since = request.args.get('since')
        base_url = self.args.protocol + "://" + request.headers["Host"] + "/"

        entities = list(self._get_file_entities(base_url))
        entities.sort(key=lambda x: x["_updated"])
        if since is None:
            return entities
        else:
            return [entity for entity in entities if entity["_updated"] > since]

    def _get_file_entities(self, base_url):
        for absfile in self._get_absfiles():
            entity = self._create_file_entity(base_url, absfile)
            if entity is not None:
                yield entity
                
    def _get_absfiles(self):
        for root, dirs, files in os.walk(self.directory):
            for d in dirs:
                yield os.path.join(root, d)
            for f in files:
                yield os.path.join(root, f)

    def _create_file_entity(self, base_url, absfile):
        relfile = os.path.relpath(absfile, start=self.directory)
        path = relfile.split(os.sep)
        # filter out files with parts starting with "." (hidden files)
        for p in path:
            if p.startswith("."):
                return

        r = os.stat(absfile)

        url = "~r%sfile/%s" % (base_url, relfile)
        updated = datetime_format(r.st_mtime_ns)

        entity = {
            "_id": relfile,
            "_updated": updated,
            "file": os.path.basename(relfile),
            "dir": os.path.dirname(relfile),
            "path": path,
            "atime": to_transit_datetime(r.st_atime_ns),
            "ctime": to_transit_datetime(r.st_ctime_ns),
            "mtime": to_transit_datetime(r.st_mtime_ns),
            "gid": r.st_gid,
            "mode": r.st_mode,
            "bytes": r.st_size,
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
    entities = data_access_layer.get_entities(request)
    return Response(json.dumps(entities), mimetype='application/json')


@app.route('/file/<path:filename>')
def get_file(filename):
    directory = os.path.abspath(data_access_layer.directory)
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run the file-share service')
    
    parser.add_argument('-p', dest='protocol', required=False, default="http",
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
    data_access_layer = DataAccess(directory, args)

    # start web server
    app.run(debug=True, host='0.0.0.0')
