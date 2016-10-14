#!/usr/bin/python           # This is client.py file

import client               # Import socket module

s = client.socket()         # Create a socket object
host = client.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done