#!/urs/bin/env python

# client -> proxy -> server

import socket
import os
# import os for proxy fork

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.bind(("0.0.0.0", 8000))
# 0.0.0.0 is special address which we can listen to all/any server
# instead of connecting to google.com, we set our address first for proxy
clientSocket.listen(5)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# this allows OS to reuse socket immediately because there are a lot of ppl using

# we will now write proxy forking
while True:
	(incomingSocket, address) = clientSocket.accept()
	print "we got a connection from %s!" % (str(address))

	pid = os.fork()
	# child will have id = 0
	if (pid == 0): # we must be the child (clone) process,
	# so we will handle proxying for this client

	# we do not need an else case here because we don't consider other cases
	# if pid != 0 then it will be parent case and will be reconnected, so no need else

# you get an error from curl since you didn't receive anything from the web but
# rather you just printed out string

		googleSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		googleSocket.connect(("www.google.ca", 80))

		incomingSocket.setblocking(0)
		googleSocket.setblocking(0)
		# tells curl to dont wait forever but just throw an error instead
		# so now we need try block

		# curl 127.0.0.1:8000 -H "Host: www.google.ca"

		# now we write proxy to server

		while True:
			# this half of the loop forwards from client to google
			skip = False
			try:
				part = incomingSocket.recv(1024)
			except socket.error, exception: # must specify specific error
				if exception.errno == 11:
					skip = True
				else:
					raise
			if not skip:
				if (len(part) > 0):
					print " > " + part
					googleSocket.sendall(part)
				else:
					exit(0)
			# this half of the loop forwards from google to client
			skip = False
			try:
				part = googleSocket.recv(1024)
			except socket.error, exception:
				if exception.errno == 11:
					skip = True
				else:
					raise
			if not skip:
				if (len(part) > 0):
					print " > " + part
					incomingSocket.sendall(part)
				else:
					exit(0)