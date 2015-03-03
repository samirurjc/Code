#!/usr/bin/python
# -*- coding: latin-1 -*-

#
# adiosApp class
# Simple web applications which just produces "Adiós, brave world!"
#
# Copyright Jesus M. Gonzalez-Barahona 2009
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# October 2009
#

import webapp

class holaApp (webapp.webApp):
    """Simple web applications which just produces 'Adiós, brave world!'"""

    def parse (self, request):
        """For this web application we don't need to parse anything"""

        return None

    def process (self, parsedRequest):
        """Process the relevant elements of the request.

        Returns 200 OK and an HTML page.
        """

        return ("200 OK", "<html><body><h1>Adiós, brave world!</h1></body></html>")


if __name__ == "__main__":
    testWebApp = holaApp ("localhost", 1234)
