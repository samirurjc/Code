#!/usr/bin/python

#
# Simple HTTP Server
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2010
# September 2009
# Febraury 2022


import socket

response = "HTTP/1.1 301 Moved Permanently\r\n" \
	+ "Location: http://gsyc.es\r\n\r\n"

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.bind(('', 1234))

    # Queue a maximum of 5 TCP connection requests
    mySocket.listen(5)

    # Accept connections, read incoming data, and answer back an HTLM page
    #  (in a loop)
    while True:
        print("Waiting for connections")
        (recvSocket, address) = mySocket.accept()
        with recvSocket:
            print("HTTP request received:")
            print(recvSocket.recv(2048))
            recvSocket.send(response.encode('ascii'))
