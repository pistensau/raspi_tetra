import serial
import time
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600

atcommand = "AT+CSQ?"
input2 = atcommand + '\r\n'
ser.write(bytes(input2.encode('ascii')))
time.sleep(0.5)

u = ser.read(20)
v = u.decode('ascii', 'ignore')

doppel = v.find(":")
komma = v.find(",")

rssi = int(v[doppel+2:komma])*2-113

print(rssi)
