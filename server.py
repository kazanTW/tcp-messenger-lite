import argparse
import socket
import threading

def handle_client(client_socket):
    def receive_messages():                                         # Define message receive on server
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f": {message}")
            except:
                break
    
    receive_thread = threading.Thread(target=receive_messages)      # Define receiving thread to let the program can work at the same time
    receive_thread.daemon = True
    receive_thread.start()

def server(ip, port):                                               # Define a server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Server listening on {ip}:{port}")

    client_socket = None

    try:
        client_socket, address = server_socket.accept()             # Wait for connection request and accept
        print(f"Accepted connection from {address}")
        handle_client(client_socket)

        while True:
            try:
                message = input()                                   # Get input
                client_socket.send(message.encode('utf-8'))
            except EOFError:                                        # Use EOF(Ctrl-D/Z) to termainte
                print("\n Server shutting down.")
                break
    except KeyboardInterrupt:                                       # Use Ctrl-C to terminate
        print("\n Server shutting down.")
    finally:                                                        # If the client_socket shutdown, server_socket shutdown
        if client_socket:
            client_socket.close()
        server_socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TCP P2P Message Server")  # Using argparse library to let program can get arguments in command line
    parser.add_argument('-a', '--address', type=str, default='0.0.0.0', help='IP address to bind to')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Port to bind to')
    args = parser.parse_args()

    server(args.address, args.port)