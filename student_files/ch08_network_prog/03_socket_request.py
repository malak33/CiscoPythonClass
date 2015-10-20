import socket

sock = socket.socket()

sock.connect(('www.yahoo.com', 80))
sock.send(b'GET / HTTP/1.0\n\n')
byte_data = sock.recv(32728)
print(byte_data.decode())
sock.close()
