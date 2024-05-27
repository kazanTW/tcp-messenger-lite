import argparse
import socket
import threading

def handle_client(client_socket):
    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f": {message}")
            except:
                break
    
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True:
            try:
                message = input()
                client_socket.send(message.encode('utf-8'))
            except EOFError:
                print("\n Server shutting down.")
                break
    except KeyboardInterrupt:
        print("\n Server shutting down.")

    client_socket.close()

def server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Server listening on {ip}:{port}")

    while True:
        try:
            client_socket, address = server_socket.accept()
            print(f"Accepted connection from {address}")
            handle_client(client_socket)
        except (EOFError, KeyboardInterrupt):
            print("\n Server shutting down.")
            server_socket.close()
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TCP P2P Message Server")
    parser.add_argument('-a', '--address', type=str, default='0.0.0.0', help='IP address to bind to')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Port to bind to')
    args = parser.parse_args()

    server(args.address, args.port)