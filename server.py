# Server Foundation
# We start by defining the server's IP address and port number. In this example, we use socket.gethostname() to get the local hostname and set the port number to 12345.
# We create a socket object and bind it to the specified IP address and port using the bind() method.
# We start listening for incoming connections using the listen() method. In this example, we set the maximum number of queued connections to 5.
# We enter an infinite loop and wait for incoming connections using the accept() method. When a connection is established, we print a message indicating where the connection came from.
# We receive data from the client using the recv() method, decode it to a string, and process the request based on its content.
# We send the response back to the client using the send() method and close the connection using the close() method.

# Security Measures
# We import the ssl module and use it to wrap the server socket with SSL/TLS security.
# We load the SSL/TLS certificate and key files using the load_cert_chain() method and pass them to the wrap_socket() method to wrap the socket with security.
# We update the listen() method to be called on the ssl_socket object that has been wrapped with security.
# We update the accept() method to be called on the ssl_socket object and create a new secure connection (conn) with the client.
# We use the secure connection (conn) to receive data from the client and send the response back to the client.
# Finally, we close the secure connection (conn) instead of the server socket (s).

import socket
import ssl

# Set the path to the security files subfolder
security_path = "ssl"

# Load the SSL certificate and key files from the security files subfolder
certfile = f"{security_path}/server.crt"
keyfile = f"{security_path}/server.key"

# Create an SSL context with the certificate and key files
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

# Create a new socket object using IPv4 addressing and TCP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port number that the server will listen on
server_ip = "127.0.0.1"
server_port = 12345

# Bind the socket to the IP address and port number
server_socket.bind((server_ip, server_port))

# Listen for incoming connections, with a maximum backlog of 5
server_socket.listen(5)

print(f"Server is listening on {server_ip}:{server_port}...")

# Wait for a client to connect
client_socket, client_address = server_socket.accept()

print(f"Client connected from {client_address[0]}:{client_address[1]}")

# Wrap the client socket with an SSL context to enable encryption
secure_client_socket = ssl_context.wrap_socket(client_socket, server_side=True)

# Receive data from the client
data = secure_client_socket.recv(1024).decode("utf-8")

# Print the received data
print(f"Received data: {data}")

# Send a response back to the client
response = "Hello from the server!"
secure_client_socket.send(response.encode("utf-8"))

# Close the connection with the client
secure_client_socket.close()

# Close the server socket
server_socket.close()