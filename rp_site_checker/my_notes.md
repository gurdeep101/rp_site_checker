**source tutorial**
https://realpython.com/site-connectivity-checker-python/#step-4-put-everything-together-in-the-apps-main-script

**various ways to check if site is online**
    * requests - too heavy and external for only 1 feature
    * urlopen() from urllib - python standard library; takes a url, opens it, gets content - to heavy for our needs
    * http_client - provides `HTTConnection` class which as `.request()` method; we use `HEAD` HTTP method. Returns only headers since we only want to check connectivity. This makes app efficient.
    