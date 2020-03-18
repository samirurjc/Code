#!/usr/bin/env python3

#
# addApp class
# Simple web application for adding numbers in two rounds
#
# Copyright Jesus M. Gonzalez-Barahona 2009-2020
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
#

import webapp

class addApp (webapp.webApp):
    """Simple web application for adding numbers in two rounds"""

    # Declare and initialize state
    #
    # Are we in first round? (receiving first addend)
    firstRound = True
    # First addend
    addend1 = 0

    def parse (self, request):
        """Return the resource name (/ removed)"""

        return request.split(' ',2)[1][1:]


    def process (self, resourceName):
        """Process the relevant elements of the request.

        Ignores requests for favicon.ico, and accepts first
        or second addend for the add.
        """

        try:
            value = int(resourceName)
        except ValueError:
            # Not an integer, bad resource
            httpCode = "400 Resource not available"
            htmlBody = "Only resources accepted: integers"
        else:
            if self.firstRound:
                self.addend1 = value
                htmlBody = "Received " + str(value) + " as first addend. " \
                    + "Waiting for second addend to add..."
            else:
                addend2 = value
                htmlBody = "Add done: " + str(self.addend1) + " + " \
                    + str(addend2) + " = " + str(self.addend1 + addend2)
            httpCode = "200 OK"
            # To finish, change to the other round
            self.firstRound = not (self.firstRound)
        return (httpCode, "<html><body>" + htmlBody + "</body></html>")


if __name__ == "__main__":
    testWebApp = addApp ("localhost", 1234)
