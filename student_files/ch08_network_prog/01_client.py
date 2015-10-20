import socket
import sys

sock = None
try:
    sock = socket.socket()
except socket.error as err:
    print('Error creating socket: {err}'.format(err=err))
    sys.exit()

try:
    sock.settimeout(5)
    server = socket.gethostname()                   # you would have to know this
    #server = '192.168.56.1'                        # you can try an IP also
    # you can also try these:  server = '127.0.0.1' or 'localhost' or '0.0.0.0'

    print('Attempting to connect to {server}...'.format(server=server))
    port = 8501
    sock.connect((server, port))            # IP sockets use (host, port) to connect
    print('Connected...')

except socket.error as err:
    print('Error connecting to server: {err}'.format(err=err))
    print('Is your server address valid or is the server running?')
    sys.exit()

try:
    byte_data = sock.recv(1024)             # blocks until data received
    print(byte_data.decode())
    sock.close()
except socket.error as err:
    print('Error receiving data: {err}'.format(err=err))
    print('Did the socket timeout?')
