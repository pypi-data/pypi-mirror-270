import serial
from pypanasonic import mewtocol

#Panasonic FP-XH serial default parameter
ser = serial.Serial(port="COM1",
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=0.5)

#Operation to PLC
if ser.is_open:
    print("\n"+ser.name)
    #Functions from the lib, get plc ver
    ser.write(mewtocol.plcVer().encode('ascii'))
    #R1 ON
    ser.write(mewtocol.switchSingleOn('R0001').encode('ascii'))

else:
    print("Serial port open fails")
