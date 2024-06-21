import asyncio
from http.client import HTTPConnection
from urllib.parse import urlparse
import aiohttp

def site_is_online(url, timeout=2):
    """
    returns true if target URL is online
    raise an exception otherwise
    2 parameters - url and seconds before timeout
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
    
async def site_is_online_async(url, timeout=2):
    """
    return true if url is online
    raise exception otherwise
    2 parameters - url and seconds before timeout
    """
    error = Exception("unkown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
    raise error