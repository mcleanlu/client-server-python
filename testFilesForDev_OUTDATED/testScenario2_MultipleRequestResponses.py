# Test case: Multiple requests and responses

import socket

# Define the server's IP address and port number
host = 'localhost'
port = 12345

# Create a socket object and connect to the server
s = socket.socket()
s.connect((host, port))

# Send multiple messages to the server
messages = ["Hello", "What's your name?", "How are you?"]
for message in messages:
    s.send(message.encode())
    response = s.recv(1024).decode()
    print(response)

# Close the socket
s.close()
