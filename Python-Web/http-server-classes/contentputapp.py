#!/usr/bin/env python3

# ContentPutApp class
# Simple web application for serving content,
# admiting PUT requests for accepting content
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

PAGE_NOT_ALLOWED = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Method not allowed: {method}.</p>
  </body>
</html>
"""

class ContentApp(webapp.webApp):

    def __init__(self, hostname, port):
        self.contents = {}
        super().__init__(hostname, port)

    def parse (self, request):
        """Return the method name and resource name"""

        data = {}
        body_start = request.find('\r\n\r\n')
        if body_start == -1:
            data['body'] = None
        else:
            data['body'] = request[body_start:]
        parts = request.split(' ', 2)
        data['method'] = parts[0]
        data['resource'] = parts[1]
        return (data)

    def process (self, data):
        """Produce the page with the content for the resource"""

        if data['method'] == 'GET':
            code, page = self.get(data['resource'])
        elif data['method'] == 'PUT':
            code, page = self.put(data['resource'], data['body'])
        else:
            code, page = "405 Method not allowed",\
                         PAGE_NOT_ALLOWED.format(method=data['method'])
        return (code, page)

    def get(self, resource):
        if resource in self.contents:
            content = self.contents[resource]
            page = PAGE.format(content=content)
            code = "200 OK"
        else:
            page = PAGE_NOT_FOUND.format(resource=resource)
            code = "404 Resource Not Found"
        return code, page

    def put(self, resource, body):
        self.contents[resource] = body
        page = PAGE.format(content=body)
        code = "200 OK"
        return code, page

if __name__ == "__main__":
    webApp = ContentApp ("localhost", 1234)
