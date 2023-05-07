# This code creates a client socket and connects to the server using the same IP address and port number as in the server-side code.
# It then sends a message to the server and receives a response, which it prints to the console.

import socket
import ssl

# Set the IP address and port number of the server to connect to
host = 'localhost'
port = 12345

# Create a socket object and wrap it with SSL/TLS security
s = socket.socket()
context = ssl.create_default_context()
s = context.wrap_socket(s, server_hostname=host)

#Connect to the server
s.connect((host, port))

# Send a message to the server
message = "Hello from the client!"
s.send(message.encode())

# Receive the response from the server
response = s.recv(1024).decode()
print(response)

# Print the response from the server
print(f"Received response: {response}")

# Close the socket
s.close()1