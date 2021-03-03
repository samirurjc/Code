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
# Session server 2.
# Serves a form, showing in the same page the last content of the form.
# This is a basic version, using POST for sending the contents of the form,
# and a cookie using a session id to track the last content submitted.

import argparse
import http.server
import http.cookies
import random
import socketserver
import string
import urllib

PORT: int = 1234

PAGE: str = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Tell me something to remember</p>
    <form action="/" method="POST">
      <input name="content" type="text" />
    <input type="submit" value="Submit" />
    </form>
    <p>The last content I remember is: {last_content}.</p>
  </body>
</html>
"""

# Dictionary for texts for each id
text: dict = {}

def parse_args () -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple HTTP Server")
    parser.add_argument('-p', '--port', type=int, default=PORT,
                        help="TCP port for the server")
    args = parser.parse_args()
    return args

class Handler(http.server.BaseHTTPRequestHandler):

    def preprocess(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")

        cookies = http.cookies.SimpleCookie(self.headers.get('Cookie'))

        if 'id' in cookies:
            id_cookie = cookies['id'].value
            self.id = id_cookie
        else:
            id_cookie = 'None'
            self.id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
            cookie = http.cookies.SimpleCookie()
            cookie['id'] = self.id
            self.send_header("Set-Cookie", cookie.output(header='', sep=''))


    def postprocess(self):

        if self.id in text:
            last_content = text[self.id]
        else:
            last_content = 'None'

        self.end_headers()
        self.wfile.write(bytes(PAGE.format(last_content=last_content),
                               'utf-8'))

    def do_POST(self):

        self.preprocess()

        if 'content-length' in self.headers:
            length_payload = int(self.headers['content-length'])
            payload = self.rfile.read(length_payload).decode("utf-8")
            qs = urllib.parse.parse_qs(payload,
                                       keep_blank_values=True)
            if 'content' in qs:
                content = qs['content'][0]
                text[self.id] = content

        self.postprocess()

    def do_GET(self):

        self.preprocess()
        self.postprocess()

def main():
    args = parse_args()
    with socketserver.TCPServer(("", args.port), Handler) as MyServer:
        print("serving at port", args.port)
        MyServer.serve_forever()

if __name__ == "__main__":
    main()
