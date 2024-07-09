# Serial import
import serial as se

# serial.Serial()
ser = se.Serial(
    port = 'COM3',
    baudrate=115200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=8
)

# serial.is_open()
ser.is_open()

# print
print(ser.name)
