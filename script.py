import serial

PORT = '/dev/ttyACM0'

ser = serial.Serial(port=PORT,baudrate=9600,timeout=1)

try:
    while True:
        message = ser.readline().decode().rsplit()
        print(f'recv {message}')
finally:
    ser.close()