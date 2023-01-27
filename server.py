import socket
import sys

srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 8089)

try:
    srv_socket.bind(addr)
except Exception as exc:
    print(f"bind failed: {exc}")
    sys.exit(1)

# https://docs.python.org/3/library/socket.html#socket.socket.listen
# Enable a server to accept connections. If backlog is specified, it must be at
# least 0 (if it is lower, it is set to 0); it specifies the number of
# unaccepted connections that the system will allow before refusing new
# connections. If not specified, a default reasonable value is chosen.

srv_socket.listen(5)
print(f"listen on address: {addr}")


while True:
    conn, addr = srv_socket.accept()
    buf = conn.recv(64)

    if len(buf) > 1:
        print(f"got data: {buf.decode()}")
    else:
        print(f"got 1 byte: {buf.decode()}")

