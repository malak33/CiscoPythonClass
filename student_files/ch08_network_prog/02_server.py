# the server
import socket
import sys

try:
    sock = socket.socket()
except socket.error as err:
    print('Error creating socket: {err}'.format(err=err))
    sys.exit()

try:
    server = socket.gethostname()
    port = 8501
    backlogQueue = 3
    sock.bind((server, port))                                   # bind to a local address
    sock.listen(backlogQueue)                                   # num connections to allow (queue) before refusing
    print('Server running on port {num}'.format(num=port))
except socket.error as err:
    print('Error binding socket to server: {err}'.format(err=err))
    print('Is your server already running?')
    sys.exit()


while True:
    client_conn, client_address = sock.accept()             # wait for an incoming connection, returns client connection and client address
    print('Client connected: ', client_address)
    client_conn.send(b'Welcome to my server!')
    client_conn.close()
