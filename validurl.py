#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2013  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/fosslc/freeseer/

import re
import httplib
import urlparse

# check if the given url has the right html format
def isValidUrl(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

# check if the given url can be reached through http request
def isExistingUrl(url):
    goodCodes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    p = urlparse.urlparse(url)
    try:
        conn = httplib.HTTPConnection(p.netloc)
        conn.request('HEAD', p.path)
        return conn.getresponse().status in goodCodes
    except StandardError:
        return False

# verify url by both applying regular expression and http request

def verifyUrl(url):
    if not isValidUrl(url):
        print "url pattern not valid"
        return False
    if not isExistingUrl(url):
        print "url doesn't exist"
        return False
    return True
