# Python Chat Application

This project is a simple **TCP-based chat application** built using Python's `socket` and `threading` modules. It includes both a **server** and a **client** with a graphical interface (GUI) for chatting, built using `tkinter`.

## Features
- Multiple clients can join the server and chat with each other.
- Clients can choose their own nicknames.
- The server broadcasts messages to all connected clients.
- The GUI allows users to send and receive messages easily.

## How It Works
- **Server**:
  - Accepts multiple client connections.
  - Broadcasts messages received from one client to all other connected clients.
  - Handles client disconnections and notifies other users when someone leaves the chat.
  
- **Client**:
  - Connects to the server.
  - Sends and receives messages in real-time.
  - Provides a simple graphical interface for chat using `tkinter`.

## Requirements
- Python 3.x
- `socket` (standard Python library)
- `threading` (standard Python library)
- `tkinter` (standard Python library for GUI)

## Installation
- **Clone the repository**:
  ```
  git clone https://github.com/gaborvida-stack/Chat-app.git
  ```
  ```
  cd Chat-app
  ```
- **Run the server**:
  ```
  python server.py
  ```
- **Run the interface**:
  ```
  python interface.py
  ```

## Usage
- **Server**: 
   - The server listens for incoming connections. By default, it binds to `0.0.0.0` on port `12345`. You can change the host and port in the `server.py` file.

- **Client**:
    - The client connects to the server by default at `127.0.0.1:12345`. You can also change the host and port in the client.py file. Upon starting, the client prompts the user for a nickname.

## Server Code Overview
- **Server class**:
    - `broadcast(message)`: Sends the message to all connected clients.
    - `handle_client(client)`: Receives messages from a client and broadcasts them.
    - `receive()`: Waits for incoming connections and starts a new thread to handle each client.

## Client Code Overview
- **ChatClient class**:
    - `gui_loop()`: Initializes the chat window using tkinter.
    - `write()`: Sends messages to the server.
    - `receive()`: Continuously listens for incoming messages from the server.
 
## Opening Firewall Ports on Linux (firewalld) 
- **To open port `12345` (or any other port you're using), you can follow these steps**:
  ```bash
  $ sudo firewall-cmd --add-port=12345/tcp --permanent
  ```
- **Reload the firewall**:
  ```bash
  $ sudo firewall-cmd --reload
  ```
