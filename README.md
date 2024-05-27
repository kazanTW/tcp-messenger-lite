# tcp-messenger-lite
A Lite CLI messenger via TCP protocol in Python.

## Requirement 
- Python >= 3.11

## Usage
### Server
```sh=
python server.py --address <server_ip> --port <server_port>
```

### Client
```sh=
python client.py --ip <server_ip> --port <server_port>
```
- If you don't add any argument, the default IP address is `0.0.0.0`, port is `8080`.
- `--address` can use `-a`, and `--port` can use `-p` instead.