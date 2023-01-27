import sys
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 8089)

try:
    client_socket.connect(('localhost', 8089))
except Exception as exc:
    print(f"unable to connect due {exc}")

payload = "hello" if len(sys.argv) < 2 else sys.argv[1]
client_socket.send(payload.encode())

