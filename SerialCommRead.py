import time
import serial
import struct
from binascii import unhexlify

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print(ser.isOpen())

if ser.is_open:
    while True:
        size = ser.inWaiting()
        if size:
            data = ser.read(8)
            print repr(data)
        else:
            print 'no data'
        time.sleep(1)
else:
    print 'serial not open'
