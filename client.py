import socket

if __name__ == '__main__':
    # name = input('Input Name: ')
    host = input('Input link host: ')
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        client.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n')
        response = client.recv(4096)
        print(response.decode())

    except EOFError:
        client.close()