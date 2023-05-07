import socket
import ssl

# Define the server's IP address and port number
host = 'localhost'
port = 12345

# Create a socket object and wrap it with SSL/TLS security
s = socket.socket()
context = ssl.create_default_context()
s = context.wrap_socket(s, server_hostname=host)
s.connect((host, port))

# Send a message to the server
message = "Hello"
s.send(message.encode())

# Receive the response from the server
response = s.recv(1024).decode()
print(response)

# Close the socket
s.close()
