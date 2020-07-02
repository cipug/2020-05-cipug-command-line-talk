# ngrok

> Public URLs for exposing your local web server

https://ngrok.com/

Not a python tool, but very handy when you need to make a local website available to someone else on the internet.

(Note: you may need to set up a free account to use this tool)

If you have a website running locally on port 8080 then run their `ngrok` binary:

    ngrok http 8080

to set up a 'tunnel' between your local 8080 port and a public port on ngrok's servers.

Provides:

* public HTTP endpoint
* public **HTTPS** endpoint
* local web interface for introspecting requests/responses

**NOTE: be aware of security when using this! Don't use for sensitive information!**

* you are running a third-party binary!
* your data is passing through their servers!


## serveo and others 

Note - there are a number of other tools that do similar jobs, in particular:

https://serveo.net/

performs a similar function using standard `ssh` rather than requiring a custom binary, eg:

    ssh -R 80:localhost:8080 serveo.net

However, I've found `serveo` less reliable and I'm hesitant to recommend...
