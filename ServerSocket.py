import socket

sock = socket.socket()
tupsock = ('0.0.0.0', 4444)


sock.bind(tupsock)

sock.listen(1)

conn, addr = sock.accept()

data = conn.recv(2048).decode()

print(data)

message = conn.send('Hi this is your server'.encode())

sock.close()
