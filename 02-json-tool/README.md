# json.tool

> JSON command-line pretty-printer

In standard library: https://docs.python.org/3/library/json.html

You've probably used the `json` module for parsing/formatting JSON.

It also exposes a handy command-line tool to tidy up JSON content:

    python -m json.tool <infile> <outfile>

and you can also use `stdin` and `stdout` so that it can be used in a shell pipeline:

    type <infile> | python -m json.tool > <outfile>

## JSON lines

NEW! As of python 3.8, the `json` module can also handle 'JSON lines' format:

* multiple JSON objects in the file / stream
* each starts on a new line
* handy for structured logging, etc.

Enable using the `--json-lines` option:

    python -m json.tool --json-lines ...

Unfortunately I'm only on 3.7...
