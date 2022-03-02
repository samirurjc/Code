#!/usr/bin/env python3

# ContentApp class
# Simple web application for serving content
#
# Copyright Jesus M. Gonzalez-Barahona 2022
# jgb @ gsyc.es
# SARO, SAT, ST subjects (Universidad Rey Juan Carlos)

import webapp

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    {content}
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

class ContentApp(webapp.webApp):

    contents = {'/': "<p>Main page</p>",
                '/hello': "<p>Hello, people</p>",
                '/bye': "<p>Bye all!!</p>"}

    def parse (self, request):
        """Return the resource name"""

        return request.split(' ',2)[1]

    def process (self, resource):
        """Produce the page with the content for the resource"""

        if resource in self.contents:
            content = self.contents[resource]
            page = PAGE.format(content=content)
            code = "200 OK"
        else:
            page = PAGE_NOT_FOUND.format(resource=resource)
            code = "404 Resource Not Found"
        return (code, page)

if __name__ == "__main__":
    webApp = ContentApp ("localhost", 1234)
