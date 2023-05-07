# Test case: Error handling

import socket

# Define the server's IP address and port number
host = 'localhost'
port = 12345

# Create a socket object and connect to the server
s = socket.socket()
s.connect((host, port))

# Send an invalid message to the server
message = "Invalid message"
s.send(message.encode())

# Receive the error response from the server
response = s.recv(1024).decode()
print(response)

# Close the socket
s.close()
