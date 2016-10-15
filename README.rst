=======================
File-share microservice
=======================

A Python micro service that exposes the content of a file system directory as a stream of JSON. This microservice can be consumed by Sesam.

::

  $ python3 service/file-share-service.py sample/projects
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5000. JSON entities can be retrieved from 'http://localhost:5000/files'.

::

  $ curl -s 'http://localhost:5000/files' | python3 -m json.tool
  [
      {
          "size": 170,
          "ctime": "~t2016-10-14T12:40:33Z",
          "path": [
              "ibm"
          ],
          "_id": "ibm",
          "file": "ibm",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T12:40:33Z",
          "dir": "",
          "mtime": "~t2016-10-14T12:40:33Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 136,
          "ctime": "~t2016-10-14T12:40:45Z",
          "path": [
              "microsoft"
          ],
          "_id": "microsoft",
          "file": "microsoft",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T12:40:45Z",
          "dir": "",
          "mtime": "~t2016-10-14T12:40:45Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T12:42:05Z",
          "path": [
              "samsung"
          ],
          "_id": "samsung",
          "file": "samsung",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T12:42:05Z",
          "dir": "",
          "mtime": "~t2016-10-14T12:42:05Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T13:34:48Z",
          "path": [
              "ibm",
              "fox"
          ],
          "_id": "ibm/fox",
          "file": "fox",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T13:34:48Z",
          "dir": "ibm",
          "mtime": "~t2016-10-14T13:34:48Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 16,
          "type": "file",
          "ctime": "~t2016-10-14T13:34:48Z",
          "path": [
              "ibm",
              "fox",
              "README.txt"
          ],
          "_id": "ibm/fox/README.txt",
          "file": "README.txt",
          "url": "~rhttp://localhost:5000/file/ibm/fox/README.txt",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T13:34:48Z",
          "dir": "ibm/fox",
          "mtime": "~t2016-10-14T13:34:48Z",
          "atime": "~t2016-10-14T18:26:29Z",
          "mode": 33188
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:26:59Z",
          "path": [
              "apple",
              "donkey"
          ],
          "_id": "apple/donkey",
          "file": "donkey",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:26:59Z",
          "dir": "apple",
          "mtime": "~t2016-10-14T18:26:59Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:27:25Z",
          "path": [
              "apple",
              "lizard"
          ],
          "_id": "apple/lizard",
          "file": "lizard",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:27:25Z",
          "dir": "apple",
          "mtime": "~t2016-10-14T18:27:25Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:27:37Z",
          "path": [
              "apple",
              "moose"
          ],
          "_id": "apple/moose",
          "file": "moose",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:27:37Z",
          "dir": "apple",
          "mtime": "~t2016-10-14T18:27:37Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 170,
          "ctime": "~t2016-10-14T18:28:06Z",
          "path": [
              "apple"
          ],
          "_id": "apple",
          "file": "apple",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:06Z",
          "dir": "",
          "mtime": "~t2016-10-14T18:28:06Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:29Z",
          "path": [
              "ibm",
              "deer"
          ],
          "_id": "ibm/deer",
          "file": "deer",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:29Z",
          "dir": "ibm",
          "mtime": "~t2016-10-14T18:28:29Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:33Z",
          "path": [
              "ibm",
              "rabbit"
          ],
          "_id": "ibm/rabbit",
          "file": "rabbit",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:33Z",
          "dir": "ibm",
          "mtime": "~t2016-10-14T18:28:33Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:42Z",
          "path": [
              "microsoft",
              "hare"
          ],
          "_id": "microsoft/hare",
          "file": "hare",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:42Z",
          "dir": "microsoft",
          "mtime": "~t2016-10-14T18:28:42Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:46Z",
          "path": [
              "microsoft",
              "wolf"
          ],
          "_id": "microsoft/wolf",
          "file": "wolf",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:46Z",
          "dir": "microsoft",
          "mtime": "~t2016-10-14T18:28:46Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:57Z",
          "path": [
              "samsung",
              "turtle"
          ],
          "_id": "samsung/turtle",
          "file": "turtle",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:57Z",
          "dir": "samsung",
          "mtime": "~t2016-10-14T18:28:57Z",
          "atime": "~t2016-10-14T19:30:29Z",
          "mode": 16877
      }
  ]
  
::

  curl -s 'http://localhost:5000/files?since=2016-10-14T18:28:42Z' | python3 -m json.tool
  [
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:46Z",
          "path": [
              "microsoft",
              "wolf"
          ],
          "_id": "microsoft/wolf",
          "file": "wolf",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:46Z",
          "dir": "microsoft",
          "mtime": "~t2016-10-14T18:28:46Z",
          "atime": "~t2016-10-14T19:30:50Z",
          "mode": 16877
      },
      {
          "size": 102,
          "ctime": "~t2016-10-14T18:28:57Z",
          "path": [
              "samsung",
              "turtle"
          ],
          "_id": "samsung/turtle",
          "file": "turtle",
          "type": "dir",
          "uid": 1030750896,
          "gid": 1235921823,
          "_updated": "2016-10-14T18:28:57Z",
          "dir": "samsung",
          "mtime": "~t2016-10-14T18:28:57Z",
          "atime": "~t2016-10-14T19:30:50Z",
          "mode": 16877
      }
  ]
  
