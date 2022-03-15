#!/usr/bin/env python3

import serial
import time


ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1, parity=serial.PARITY_NONE,
                    bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE)


# ser.open()
ser.write("*IDN?\n".encode(encoding='utf-8'))
ser.flush()
time.sleep(1)
ser.write("*RST".encode(encoding='utf-8'))
ser.flush()
time.sleep(1)
ser.write("*CLS".encode(encoding='utf-8'))
ser.flush()

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
    ser.write((line+'\n').encode('utf-8'))
    ser.flush()
    time.sleep(0.3)
    resp = ser.read_until(expected='\n')
    reply.append(str(resp))
print('\n'.join(reply))


ser.close()
