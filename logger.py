from __future__ import print_function
from time import gmtime, strftime, sleep
import serial
ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
if ser.isOpen():
    print("Otwarty")
else:
    print("Port nie otwarty")
    exit(1)
ser.flushInput()
while True:
    line = ser.readline()
    if line != '':
        print(strftime("'%d %b %Y %H:%M:%S',", gmtime())+line, end='')
