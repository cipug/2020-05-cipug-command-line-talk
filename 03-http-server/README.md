# http.server

> simple standalone HTTP server

In standard library: https://docs.python.org/3/library/http.server.html

You can run a **very** basic HTTP server directly on the command-line:

    python -m http.server <port>

(NOTE: in python 2 this module was called `SimpleHTTPServer`)

Defaults to serving the current directory, but you can specify an alternate one:

    python -m http.server <port> --directory <path>

**NOT SAFE FOR PRODUCTION USE!!!** - but handy on occasion :)

## ComplexHTTPServer

NOTE: the standard `http.server` is **single-threaded** - it will only process one request at a time.

There is a modified version that is multithreaded:

    https://github.com/vickysam/ComplexHTTPServer

but this is not part of the standard library, so install it, eg:

    poetry add ComplexHTTPServer

Then you run it in a very similar way:

    python -m ComplexHTTPServer <port>

...but note - you may need to kill it using task manager :)
