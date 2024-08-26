# Chat Server and Client

This repository contains a simple chat application implemented in Python using sockets. The application is composed of a server and client, enabling real-time text-based communication.

## Overview

- **Server:** Manages multiple client connections, handles message broadcasting, and manages client disconnections.
- **Client:** Connects to the server, sends messages, and receives messages from other clients.

## Server

The server script is responsible for:

- **Listening for Connections:** The server listens on a specified port for incoming client connections.
- **Client Management:** Once a connection is established, the server handles each client in a separate thread, allowing simultaneous communication.
- **Message Broadcasting:** The server broadcasts received messages to all connected clients, ensuring that all participants in the chat are updated in real-time.
- **Client Disconnection:** When a client disconnects, the server handles the disconnection, removes the client from the active list, and notifies other clients.

## Client

The client script provides:

- **Connection to Server:** The client connects to the server using the server's IP address and port.
- **Nickname Assignment:** Upon connection, the client is prompted to choose a nickname, which is sent to the server for identification.
- **Sending and Receiving Messages:** The client allows the user to send messages to the server, which then broadcasts them to all connected clients. Additionally, it continuously receives and displays messages from the server.

## How It Works

1. **Start the Server:** Run the server script to initialize and start listening for incoming connections.
2. **Run the Client:** Execute the client script to connect to the server, enter a nickname, and start sending and receiving messages.

## Features

- **Real-time Communication:** Supports real-time chat between multiple clients.
- **Thread Management:** Uses threading to handle multiple clients simultaneously.
- **Nickname Handling:** Each client can choose a unique nickname to identify themselves in the chat.

## Requirements

- Python 3.x

## Usage

1. **Server Setup:** Launch the server script first to set up the chat server.
2. **Client Interaction:** Run the client script on multiple instances to connect to the server and begin chatting.

## Notes

- Ensure that the server is running before starting any clients.
- The client’s nickname is used to identify messages in the chat.

Feel free to explore the code and modify it as needed for your own chat application needs.
