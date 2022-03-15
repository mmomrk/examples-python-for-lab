#!/usr/bin/env python3

import socket
import sys
import time


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock = socket.socket()
except socket.error:
    print("Socket init err. I'm dying")
    sys.exit()

try:
    ip = socket.gethostbyname("moxa-nport1.phys.funsci.bmstu.ru")
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print("Resolved moxa to ip ", ip)
print("Socket is ", sock)
params = (ip, 4001)
print("params", params)
sock.connect(params)
print("connected to ", sock)

try:
    sock.sendall(b"*idn?\r")
except socket.error:
    print("Failed to send all")
    sys.exit()
except AttributeError:
    print("Not this again")
    sys.exit()


def getRepl():
    global sock
    reply = sock.recv(4444)
    print(reply)
    data = ''
    while b'\n' not in reply:
        print(reply)
        data += reply.decode("utf-8")
        reply = sock.recv(4444)
    print("Gott reply\n", data)
    return data


getRepl()

# sock.open()
sock.sendall("*IDN?\n".encode(encoding='utf-8'))
time.sleep(1)
getRepl()
sock.sendall("*RST".encode(encoding='utf-8'))
time.sleep(1)
sock.sendall("*CLS".encode(encoding='utf-8'))

commands = ":SOUR:FUNC:MODE VOLT\n\
:SOUR:VOLT:MODE FIX\n\
:SOUR:VOLT:LEV 0\n\
:SOUR:VOLT:RANG:AUTO 1\n\
:SENS:FUNC \"CURR\"\n\
:SENS:CURR:RANGE:AUTO 1\n\
:SENS:VOLT:RANGE:AUTO 1\n\
:SENS:CURR:PROT 0.001\n\
:OUTP ON\n\
:READ?\n\
:SOUR:VOLT:LEV 0.1\n\
:READ?\n\
:SOUR:VOLT:LEV 0.2\n\
:READ?\n\
:SOUR:VOLT:LEV 0.3\n\
:READ?\n\
:SOUR:VOLT:LEV 0.4\n\
:READ?\n\
:SOUR:VOLT:LEV 0.5\n\
:READ?\n\
:SOUR:VOLT:LEV 1.5\n\
:READ?\n\
:OUTP OFF\n\
:SOUR:VOLT:LEV 0.\n\
"
reply = []
for line in commands.split('\n'):
    print(line)
    sock.sendall((line+'\n').encode('utf-8'))
    time.sleep(0.3)
    if '?' in line:
        reply.append(getRepl())
print('\n'.join(reply))


sock.close()
