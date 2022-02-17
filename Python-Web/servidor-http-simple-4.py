#!/usr/bin/python

#
# Simple HTTP Server (version 2: reuses the port, so it can be
#  restarted right after it has been killed. Accepts connects from
#  the outside world, and from localhost, by binding to
#  all interfaces of the host.
#
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT courses (Universidad Rey Juan Carlos)
# September 2010
# September 2009
# Febraury 2022

import socket

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as mySocket:
    # Let the port be reused if no process is actually using it
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind to the address corresponding to the main name of the host
    mySocket.bind(('',1236))

    # Queue a maximum of 5 TCP connection requests

    mySocket.listen(5)

    # Accept connections, read incoming data, and answer back an HTLM page
    #  (in a loop)

    while True:
        print("Waiting for connections")
        (recvSocket, address) = mySocket.accept()
        print("Request received:")
        print(recvSocket.recv(2048))
        print("Answering back...")
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello World!</h1>" +
                        b"<p>And in particular hello to you, " +
                        str(address[0]).encode('ascii') +
                        b"</p>" +
                        b"</body></html>" +
                        b"\r\n")
        recvSocket.close()

        
