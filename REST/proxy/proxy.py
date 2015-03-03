#!/usr/bin/python

#
# Proxy class
# Simple web application for proxying to the web
# Accepts "GET /resource", and returns the content of
#   http://resource. For example, if /gsyc.es is used,
#   it returns the content of http://gsyc.es
#
# Copyright Jesus M. Gonzalez-Barahona 2009
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# March 2015
#

import webapp
import urllib

class proxyApp (webapp.webApp):
    """Simple web application for proxying to the web."""

    def parse (self, request):
        """Return the resource name (/ removed)"""

        return request.split(' ',2)[1][1:]


    def process (self, resourceName):
        """Process the relevant elements of the request.

        """

        try:
            f = urllib.urlopen ("http://" + resourceName)
            httpBody = f.read()
            httpCode = "200 OK"
        except IOError:
            httpBody = "Error: could not connect"
            httpCode = "404 Resource Not Available"
        return (httpCode, httpBody)


if __name__ == "__main__":
    testProxyApp = proxyApp ("localhost", 1234)
