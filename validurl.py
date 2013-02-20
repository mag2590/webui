import re
import httplib
import urlparse

def isValidUrl(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

def isExistingUrl(url):
    goodCodes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    p = urlparse.urlparse(url)[1:3]
    try:
        conn = httplib.HTTPConnection(p.netloc)
        conn.request('HEAD', p.path)
        return conn.getresponse().status in goodCodes
    except StandardError:
        return False


def verifyUrl(url):
    return isValidUrl(url) and isExistingUrl(url)
