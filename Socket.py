import socket

# sock = socket.socket()

# sock.connect(("IP", "port"))
# sock.connect(("192.168.56.101", 4444))
#
## sock.send('Hello server, I am a client you like'.encode())
#
#
# sock.close()



# sock.bind(('0.0.0.0', 4444))
# sock.listen(4)
# conn,addr = sock.accept()
# print(conn)
# print("\n\n\n\n")
# print(addr)
sock = socket.socket()

sock.connect(('127.0.0.1', 4444))

sock.send('Hello kind server, Im client you like'.encode())

message = sock.recv(2048).decode()

print(message)

sock.close()