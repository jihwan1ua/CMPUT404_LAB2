#!/usr/bin/env python

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# the second argument represents TCP socket for streaming

clientSocket.connect(("www.google.com", 80))

# why are there 2 patenthesis? because it is like C programming style.

clientSocket.sendall("GET / HTTP/1.0\r\n\r\n")

# the \r\n\r\n stuff should be there and it should be backslashed

# we are skipping all the headers in this exercise
# if we want to curl or request it will look like this
while True:
	part = clientSocket.recv(1024)
	if (len(part) > 0):
		print part
	# if we get an empty string it means the connection is done, so we exit
	else: # part will be "" when the connection is done
		exit(0)

# we will now program proxy
# Client -> Proxy -> Server, proxy will retrieve information and access to blocked Server then
# will respond it back to the Client