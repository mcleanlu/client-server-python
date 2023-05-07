import socket

# Create a new socket object
s = socket.socket()

# Get the local hostname
host = 'localhost'

# Set the port number
port = 12345

# Bind the socket to the address and port
s.bind((host, port))

print("Socket bound to port", port)
