**source tutorial**

https://realpython.com/site-connectivity-checker-python/#step-4-put-everything-together-in-the-apps-main-script

**various ways to check if site is online**

* requests - too heavy and external for only 1 feature  
* urlopen() from urllib - python standard library; takes a url, opens it, gets content as a `Request` object - to heavy for our needs since it loads the whole page.
* `http.client` module - provides `HTTPConnection` class which has `.request()` method
    * `.request()` method allows us to perform HTTP requests using different HTTP methods.
    * we use `HEAD` HTTP method. Returns only headers since we only want to check connectivity. This makes app efficient.

**App Construct**

* checker.py - has the function to check connectivity
* cli.py - pass cli options
* __main__.py - entry point script; connects CLI in front-end with connectivity checking functionality in backend.
    * Including an __main__.py enables us to run packages as an executable program
    