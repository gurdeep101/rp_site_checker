from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """
    returns true if target URL is online
    raise an exception otherwise
    """
    error = Exception("Unknown error")
    # parse url
    parser = urlparse(url)
    # extract hostname from target url
    host = parser.netloc or parser.path.split("/")[0]
    # check if site is available over http or https ports
    for port in (80, 443):
        # create an HTTP connection
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            # request head and return if true
            connection.request("HEAD","/")
            return True
        # keep reference to the exception error
        except Exception as e:
            error = e
        # close the connection
        finally:
            connection.close()
        # raise error if HEAD request is not successful
        raise error