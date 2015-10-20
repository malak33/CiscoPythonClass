# creating a telnet client is tricky as it requires knowing
# exactly how the server will respond
# then stopping the read process when that response is encountered

from getpass import getpass
from telnetlib import Telnet

host = 'ip_address'
prompt = '$'
username = input('Enter your remote username: ')
pswd = getpass()

tn = Telnet(host)

tn.read_until('login: ')
tn.write(username + '\n')
if pswd:
   tn.read_until('Password: ')
   tn.write(pswd + '\n')

tn.read_until(prompt)
tn.write('ls\n')
tn.read_until(prompt)
tn.write('exit\n')
