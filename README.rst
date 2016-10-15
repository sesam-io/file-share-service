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

  $ python3 service/file-share-service.py sample/projects
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5000. JSON entities can be retrieved from 'http://localhost:5000/files'.

::

  $ curl -s 'http://localhost:5000/files' | jq . -S
  [
    {
      "_id": "ibm",
      "_updated": "2016-10-14T12:40:33Z",
      "atime": "~t2016-10-15T10:37:56Z",
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
      "atime": "~t2016-10-15T10:37:56Z",
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
      "atime": "~t2016-10-15T10:37:56Z",
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
      "_id": "ibm/fox",
      "_updated": "2016-10-14T13:34:48Z",
      "atime": "~t2016-10-15T10:37:56Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T13:34:48Z",
      "dir": "ibm",
      "file": "fox",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T13:34:48Z",
      "path": [
        "ibm",
        "fox"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "apple/donkey",
      "_updated": "2016-10-14T18:26:59Z",
      "atime": "~t2016-10-15T10:37:56Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:26:59Z",
      "dir": "apple",
      "file": "donkey",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:26:59Z",
      "path": [
        "apple",
        "donkey"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "apple/lizard",
      "_updated": "2016-10-14T18:27:25Z",
      "atime": "~t2016-10-15T10:37:56Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:27:25Z",
      "dir": "apple",
      "file": "lizard",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:27:25Z",
      "path": [
        "apple",
        "lizard"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "apple/moose",
      "_updated": "2016-10-14T18:27:37Z",
      "atime": "~t2016-10-15T10:37:56Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:27:37Z",
      "dir": "apple",
      "file": "moose",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:27:37Z",
      "path": [
        "apple",
        "moose"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "apple",
      "_updated": "2016-10-14T18:28:06Z",
      "atime": "~t2016-10-15T10:37:56Z",
      "bytes": 170,
      "ctime": "~t2016-10-14T18:28:06Z",
      "dir": "",
      "file": "apple",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:28:06Z",
      "path": [
        "apple"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "ibm/deer",
      "_updated": "2016-10-14T18:28:29Z",
      "atime": "~t2016-10-15T10:37:56Z",
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
      "atime": "~t2016-10-15T10:37:56Z",
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
      "atime": "~t2016-10-15T10:37:56Z",
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
      "_id": "microsoft/wolf",
      "_updated": "2016-10-14T18:28:46Z",
      "atime": "~t2016-10-15T10:37:56Z",
      "bytes": 102,
      "ctime": "~t2016-10-14T18:28:46Z",
      "dir": "microsoft",
      "file": "wolf",
      "gid": 1235921823,
      "mode": 16877,
      "mtime": "~t2016-10-14T18:28:46Z",
      "path": [
        "microsoft",
        "wolf"
      ],
      "type": "dir",
      "uid": 1030750896
    },
    {
      "_id": "samsung/turtle",
      "_updated": "2016-10-14T18:28:57Z",
      "atime": "~t2016-10-15T10:37:56Z",
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
      "atime": "~t2016-10-15T10:35:54Z",
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
    }
  ]
  
::

  $ curl -s 'http://localhost:5000/files?since=2016-10-14T18:28:46Z' | jq . -S
  [
    {
      "_id": "samsung/turtle",
      "_updated": "2016-10-14T18:28:57Z",
      "atime": "~t2016-10-15T10:37:51Z",
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
      "atime": "~t2016-10-15T10:35:54Z",
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
    }
  ]
  
Docker
------

Building:

::

  $ docker build -t sesam/file-share-service .

Running:

::

  $ docker run --name file-share-service --rm -it -p 5000:5000 -v $PWD/sample/projects:/file-share sesam/file-share-service
 
