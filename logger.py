from __future__ import print_function
from time import gmtime, strftime, sleep
import serial
import os
from serial.tools import list_ports
import argparse

import argparse

def list_serial_ports():
    # Windows
    if os.name == 'nt':
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append('COM'+str(i + 1))
                s.close()
            except serial.SerialException:
                pass
        return available
    else:
        # Mac / Linux
        return [port[0] for port in list_ports.comports()]
def print_serial_ports():
    ret = list_serial_ports()
    print('\n'.join(ret))
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help='List serial ports and stop', action='store_true')
parser.add_argument("-p", "--port", help='Serial port used to listen to', default='/dev/ttyACM0')
args = parser.parse_args()
if args.list:
    print_serial_ports();
    exit(0);

port=args.port
    
ser = serial.Serial(port,9600, timeout=1)
if ser.isOpen():
    print("Otwarty")
else:
    print("Port nie otwarty")
    exit(1)
sleep(1)
ser.flushInput()
while True:
    line = ser.readline()
    if line != '':
        print(strftime("'%d %b %Y %H:%M:%S',", gmtime())+line, end='')
