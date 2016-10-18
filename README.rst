=======================
File-share microservice
=======================

A Python micro service that exposes the content of a file system directory as a stream of JSON. This microservice can be consumed by Sesam.

::

  $ python3 service/file-share-service.py --help
  usage: file-share-service.py [-h] [-p PROTOCOL] [directory]
  
  Run the file-share service.
  
  positional arguments:
    directory    the directory to serve
  
  optional arguments:
    -h, --help   show this help message and exit
    -p PROTOCOL  the protocol used refer back to the service (default is "http")

Example
-------

::

  $ python3 service/file-share-service.py sample/portfolio
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5000. JSON entities can be retrieved from 'http://localhost:5000/files'.

The commands below uses `curl <https://curl.haxx.se/>`_ to send the requests and `jq <https://stedolan.github.io/jq/>`_ to prettify the response.

Get all the files and directories:

::

  $ curl -s 'http://localhost:5000/files' | jq . -S
  [
    {
      "_id": "ibm",
      "_updated": "2016-10-14T12:40:33Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 170,
      "ctime": "~t2016-10-14T12:40:33Z",
      "dir": "",
      "file": "ibm",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T12:40:33Z",
      "path": [
        "ibm"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "microsoft",
      "_updated": "2016-10-14T12:40:45Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 136,
      "ctime": "~t2016-10-14T12:40:45Z",
      "dir": "",
      "file": "microsoft",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T12:40:45Z",
      "path": [
        "microsoft"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "samsung",
      "_updated": "2016-10-14T12:42:05Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T12:42:05Z",
      "dir": "",
      "file": "samsung",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T12:42:05Z",
      "path": [
        "samsung"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "ibm/deer",
      "_updated": "2016-10-14T18:28:29Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:28:29Z",
      "dir": "ibm",
      "file": "deer",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:28:29Z",
      "path": [
        "ibm",
        "deer"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "ibm/rabbit",
      "_updated": "2016-10-14T18:28:33Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:28:33Z",
      "dir": "ibm",
      "file": "rabbit",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:28:33Z",
      "path": [
        "ibm",
        "rabbit"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "microsoft/hare",
      "_updated": "2016-10-14T18:28:42Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:28:42Z",
      "dir": "microsoft",
      "file": "hare",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:28:42Z",
      "path": [
        "microsoft",
        "hare"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "samsung/turtle",
      "_updated": "2016-10-14T18:28:57Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:28:57Z",
      "dir": "samsung",
      "file": "turtle",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:28:57Z",
      "path": [
        "samsung",
        "turtle"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "ibm/fox/README.txt",
      "_updated": "2016-10-15T08:11:11Z",
      "atime": "~t2016-10-17T07:26:21Z",
      "bytes": 16,
      "ctime": "~t2016-10-15T08:11:11Z",
      "dir": "ibm/fox",
      "file": "README.txt",
      "gid": 1235921823,
      "mode": 33188,
      "mtime": "~t2016-10-15T08:11:11Z",
      "path": [
        "ibm",
        "fox",
        "README.txt"
      ],
      "type": "file",
      "uid": 1030750896,
      "url": "~rhttp://localhost:5000/file/ibm/fox/README.txt"
    },
    {
      "_id": "microsoft/wolf",
      "_updated": "2016-10-17T07:27:04Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 136,
      "ctime": "~t2016-10-17T07:27:04Z",
      "dir": "microsoft",
      "file": "wolf",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-17T07:27:04Z",
      "path": [
        "microsoft",
        "wolf"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "microsoft/wolf/README.txt",
      "_updated": "2016-10-17T07:27:04Z",
      "atime": "~t2016-10-17T07:29:02Z",
      "bytes": 17,
      "ctime": "~t2016-10-17T07:27:04Z",
      "dir": "microsoft/wolf",
      "file": "README.txt",
      "gid": 1235921823,
      "mode": 33188,
      "mtime": "~t2016-10-17T07:27:04Z",
      "path": [
        "microsoft",
        "wolf",
        "README.txt"
      ],
      "type": "file",
      "uid": 1030750896,
      "url": "~rhttp://localhost:5000/file/microsoft/wolf/README.txt"
    },
    {
      "_id": "ibm/fox",
      "_updated": "2016-10-17T07:28:53Z",
      "atime": "~t2016-10-17T07:30:42Z",
      "bytes": 136,
      "ctime": "~t2016-10-17T07:28:53Z",
      "dir": "ibm",
      "file": "fox",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-17T07:28:53Z",
      "path": [
        "ibm",
        "fox"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "ibm/fox/participants.csv",
      "_updated": "2016-10-17T07:28:53Z",
      "atime": "~t2016-10-17T07:29:42Z",
      "bytes": 48,
      "ctime": "~t2016-10-17T07:28:53Z",
      "dir": "ibm/fox",
      "file": "participants.csv",
      "gid": 1235921823,
      "mode": 33188,
      "mtime": "~t2016-10-17T07:28:53Z",
      "path": [
        "ibm",
        "fox",
        "participants.csv"
      ],
      "type": "file",
      "uid": 1030750896,
      "url": "~rhttp://localhost:5000/file/ibm/fox/participants.csv"
    }
  ]

Now get only the files and directories modified made after a specific point in time:

::

  $ curl -s 'http://localhost:5000/files?since=2016-10-17T07:27:04Z' | jq . -S
  [
    {
      "_id": "ibm/fox",
      "_updated": "2016-10-17T07:28:53Z",
      "atime": "~t2016-10-17T07:31:49Z",
      "bytes": 136,
      "ctime": "~t2016-10-17T07:28:53Z",
      "dir": "ibm",
      "file": "fox",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-17T07:28:53Z",
      "path": [
        "ibm",
        "fox"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "ibm/fox/participants.csv",
      "_updated": "2016-10-17T07:28:53Z",
      "atime": "~t2016-10-17T07:29:42Z",
      "bytes": 48,
      "ctime": "~t2016-10-17T07:28:53Z",
      "dir": "ibm/fox",
      "file": "participants.csv",
      "gid": 1235921823,
      "mode": 33188,
      "mtime": "~t2016-10-17T07:28:53Z",
      "path": [
        "ibm",
        "fox",
        "participants.csv"
      ],
      "type": "file",
      "uid": 1030750896,
      "url": "~rhttp://localhost:5000/file/ibm/fox/participants.csv"
    }
  ]

If the entity contains the "url" property, then the contents of the file can be downloaded. The last one in the previous response, "ibm/fox/README.txt", has one and can be downloaded like this:

::

   $ curl -s 'http://localhost:5000/file/ibm/fox/README.txt'
   Hello, I'm Fox!

Docker
------

Building:

::

  $ docker build -t sesam/file-share-service .

Running:

::

  $ docker run --name file-share-service --rm -it -p 5000:5000 -v $PWD/sample/portfolio:/file-share sesam/file-share-service
