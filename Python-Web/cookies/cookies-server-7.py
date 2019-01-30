#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Simple HTTP Server
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# January 2019
#
# Important: Run with Python 3.6 or higher
#
# Server sending a cookie when the content of the text form
# is received, and showing in the screen the text in the
# cookie (if any).

import argparse
import http.server
import http.cookies
import random
import socketserver
import string
import urllib

PORT = 1234

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Hello!</p>
    <form action="/" method="GET">
      Say something: <input name="something" type="text" />
    <input type="submit" value="Submit" />
    <p>{}</p>
    <p>{}</p>
    <p>{}</p>
    <p>{}</p>
    </form>
  </body>
</html>
"""

# Dictionary for texts for each id
text = {}

def parse_args ():
    parser = argparse.ArgumentParser(description="Simple HTTP Server")
    parser.add_argument('-p', '--port', type=int, default=PORT,
                        help="TCP port for the server")
    args = parser.parse_args()
    return args

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print("Received: GET " + self.path)
        parsed_resource = urllib.parse.urlparse(self.path)

        self.send_response(200)
        self.send_header("Content-type", "text/html")

        cookies = http.cookies.SimpleCookie(self.headers.get('Cookie'))

        yousaid_cookie = ""
        if 'yousaid' in cookies:
            yousaid_cookie = "Cookie (yousaid): " + cookies['yousaid'].value

        id_text = ""
        if 'id' in cookies:
            id = cookies['id'].value
            id_text = "Cookie (id): " + id
        else:
            id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
            cookie = http.cookies.SimpleCookie()
            cookie['id'] = id
            self.send_header("Set-Cookie", cookie.output(header='', sep=''))

        yousaid_text = ""
        if parsed_resource.query:
            qs = urllib.parse.parse_qs(parsed_resource.query)
            if 'something' in qs:
                you_said = qs['something'][0]
                yousaid_text = "You said: " + you_said
                cookie = http.cookies.SimpleCookie()
                cookie['yousaid'] = you_said
                self.send_header("Set-Cookie", cookie.output(header='', sep=''))
                text[id] = you_said

        yousaid_id = ""
        if id in text:
            yousaid_id = "Last text in form (from id): " + text[id]

        self.end_headers()
        self.wfile.write(bytes(PAGE.format(yousaid_text, yousaid_cookie, id_text, yousaid_id),
                               'utf-8'))

def main():
    args = parse_args()
    with socketserver.TCPServer(("", args.port), Handler) as MyServer:
        print("serving at port", args.port)
        MyServer.serve_forever()

if __name__ == "__main__":
    main()
