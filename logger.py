from __future__ import print_function
from time import gmtime, strftime, sleep
import serial
ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
if ser.isOpen():
    print("Otwarty")
sleep(2)
while True:
    line = ''
    while ser.inWaiting() > 0:
        ret = ser.read(1)
        line += ret
        if ret == '\n':
            break
    if line != '':
        print(strftime("'%d %b %Y %H:%M:%S',", gmtime())+line, end='')
