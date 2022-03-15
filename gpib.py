#!/usr/bin/env python3

#import serial
import Gpib
import time


#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE)
kkk = Gpib.Gpib("KEITHLEY___")


# ser.open()
# ser.write("*IDN?\n".encode(encoding='utf-8'))
print("IDN")
kkk.write("*IDN?\n".encode(encoding='utf-8'))
# ser.flush()
print("Read")
time.sleep(1)
kkk.read()
time.sleep(1)
# ser.write("*RST".encode(encoding='utf-8'))
print("RST")
kkk.write("*RST\n".encode(encoding='utf-8'))
# ser.flush()
time.sleep(1)
print("CLS")
# ser.write("*CLS".encode(encoding='utf-8'))
kkk.write("*CLS\n".encode(encoding='utf-8'))
# kkk.flush()
time.sleep(1)

# commands=":SOUR:FUNC:MODE VOLT\n\
commands = ":SOUR:FUNC VOLT\n\
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
print("BEFORE")
kkk.write(":SOUR:FUNC VOLT\n")
time.sleep(1)
print("AFTER")

reply = []
for line in commands.split('\n'):
    nline = line+'\n'
    print(nline)
    # ser.write((line+'\n').encode('utf-8'))
    # kkk.write(nline.encode('utf-8'))
    kkk.write(nline)
    # ser.flush()
    time.sleep(0.3)
    # resp=ser.read_until(expected='\n')
    if "READ" in nline:
        resp = kkk.read()
        reply.append(str(resp))
print('\n'.join(reply))

kkk.close()
# ser.close()
