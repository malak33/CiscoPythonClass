from ftplib import FTP, error_perm
import socket
import sys


host = 'ftp1.freebsd.org'
dir_name = '/pub/FreeBSD'
file_name = 'README.TXT'

try:
    ftp_conn = FTP(host)
except (socket.error, socket.gaierror) as e:
    print('Error reaching {0} (reason: {1})'.format(host, e))
    sys.exit(42)

print('\n---Connected to {0}\n'.format(host))

try:
    ftp_conn.login()
except error_perm as e:
    print('Error logging in (reason: {0})'.format(e))
    ftp_conn.quit()
    sys.exit()

print('---Anonymously logged in')

try:
    ftp_conn.cwd(dir_name)
except error_perm as e:
    print('Error logging in (reason: {0})'.format(e))
    ftp_conn.quit()
    sys.exit()

print('---Changed to {0}'.format(dir_name))

files = []
ftp_conn.dir(files.append)

for file in files:
    print(file)

try:
    ftp_conn.retrbinary('RETR ' + file_name, open(file_name, 'wb').write)
except error_perm as e:
    print('Could not retrieve {0} (reason: {1})'.format(file_name, e))
else:
    print('----Downloaded {0}'.format(file_name))

ftp_conn.quit()
