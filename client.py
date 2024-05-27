import argparse
import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f": {message}")
        except:
            break

def client(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True:
            try:
                message = input()
                client_socket.send(message.encode('utf-8'))
            except EOFError:
                print("\nClient exit.")
                break
    except KeyboardInterrupt:
        print("\nClient exit.")

    client_socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TCP P2P Message Client")
    parser.add_argument('-a', '--address', type=str, default='0.0.0.0', help='IP address to bind to')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Port to bind to')
    args = parser.parse_args()

    client(args.address, args.port)
