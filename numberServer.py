#!/usr/bin/python           # This is server.py file

import number               # Import socket module

s = number.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   clientsocket, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   clientsocket.send('Thank you for connecting')
   clientsocket.close()                # Close the connection