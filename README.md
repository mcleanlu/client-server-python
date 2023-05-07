# Overview

I wanted to learn more about network programming and how to build a safe server utilizing SSL/TLS encryption because I'm a software developer. To do this, I developed a networking software in Python that uses SSL/TLS encryption and the client-server paradigm.

A client can connect to a server using my networking software's secure SSL/TLS connection. The client connects to the server by utilizing the same IP address and port number that the server uses to listen for incoming connections. Once connected, the client can communicate with the server by sending messages, which the server will then process and respond to.

This software was created in order to learn more about network programming and how to use Python to construct SSL/TLS encryption. In order to prevent sensitive data from being intercepted, I also wanted to understand how to establish secure connections between clients and servers.


[Software Demo Video](https://drive.google.com/file/d/1iIOW2VMDdAA9GIeu6LE6tqAM058p5Vo3/view?usp=sharing)

# Network Communication

I used the client-server architecture, the TCP/IP protocol, and SSL/TLS encryption for this networking program. The client connects to the server by utilizing the same IP address and port number that the server uses to listen for incoming connections.

Although they are sent in plain text, the communications are encrypted with SSL/TLS to ensure safe communication between the client and server.

# Development Environment

I utilized Python as my programming language, Visual Studio Code as my IDE, and the socket and ssl packages to implement SSL/TLS encryption and the client-server concept in this networking program.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python socket programming tutorial](https://realpython.com/python-sockets/)
* [Python ssl library documentation](https://docs.python.org/3/library/ssl.html)

# Future Work

I want to expand the networking program's capability in the future by enabling file transfers between the client and server, for example. By adopting more sophisticated authentication mechanisms and stronger encryption techniques, I would also wish to increase the program's security. Finally, I want to add a graphical user interface to the application to make it more user-friendly.