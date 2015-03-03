#!/usr/bin/python

#
# addApp class
# Simple web application for adding numbers in two rounds
#
# Copyright Jesus M. Gonzalez-Barahona 2009
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# October 2009
#

import webapp

class shortenerApp (webapp.webApp):
    """Simple web application for shortening urls"""

    def parse (self, request):
        """Return the resource name (/ removed)"""

        lines = request.splitlines()
        firstLineWords = lines[0].split(' ',2)
        verb = firstLineWords[0]
        resource = firstLineWords[1]
        separator = lines.index ('')
        try:
            bodyFirstLine = lines[separator+1]
        except IndexError:
            bodyFirstLine = None
        return (verb, resource, bodyFirstLine)


    def process (self, reqData):
        """Process the relevant elements of the request.

        Ignores requests for favicon.ico, and accepts first
        or second addend for the add.
        """

        (verb, resource, reqBody) = reqData
        print reqData
        if verb == "GET":
            if resource == "/":
                htmlBody = """
<form action="/" method="post">
url to shorten: <input type="text" name="url">
<input type="submit" value="Submit">
</form> """
                httpCode = "200 OK"
            else:
                htmlBody = "Redirect"
                httpCode = "200 OK"
        elif verb == "POST":
            params = reqBody.split('&')
            url = None
            for param in params:
                (name, value) = param.split("=", 1)
                if name == "url":
                    url = value
                    exit
            htmlBody = str(url)
            httpCode = "200 OK"
        return (httpCode, "<html><body>" + htmlBody + "</body></html>")


if __name__ == "__main__":
    testWebApp = shortenerApp ("localhost", 1234)
