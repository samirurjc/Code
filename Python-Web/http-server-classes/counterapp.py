#!/usr/bin/env python3

#
# counterApp class
# Simple web application for counting
#
# Copyright Jesus M. Gonzalez-Barahona 2020
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
#

import webapp

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Countdown!</p>
    <p>Current count: {count}.</p>
  </body>
</html>
"""

PAGE_NOT_FOUND = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Resource not found: {resource}.</p>
  </body>
</html>
"""


class counterApp (webapp.webApp):
    """Simple web application for counting"""

    # Declare and initialize state
    count = 5

    def parse (self, request):
        """Return the resource name"""

        return request.split(' ',2)[1]


    def process (self, resourceName):
        """Process the relevant elements of the request.

        Ignores everything except for '/'.
        """

        if resourceName == '/':
            htmlBody = PAGE.format(count=str(self.count))
            self.count = (self.count - 1) % 6
            httpCode = "200 OK"
        else:
            htmlBody = PAGE_NOT_FOUND.format(resource=resourceName)
            httpCode = "404 Resource Not Found"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    webApp = counterApp ("localhost", 1234)
