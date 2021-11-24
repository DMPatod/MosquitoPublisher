from paho import mqtt
import serial
from paho.mqtt import client as mqtt_client

PORT = '/dev/ttyUSB0'

ser = serial.Serial(port=PORT, baudrate=115200, timeout=None)

publisher = mqtt_client.Client("RaspberrPI")
publisher.connect(host="192.168.1.102", port=1883, keepalive=60, bind_address="")

topics = ["sensorA/current","sensorA/voltage","sensorB/current","sensorB/voltage","sensorC/current","sensorC/voltage"]

try:
    retry = 0
    while retry < 3:
        while True:
            message = ser.readline().decode()
            print(f'recv {message}')
            if message[0] == '#':
                message = message.split(',')
                index = 1
                for val in topics:
                    publisher.publish(val,message[index])
                    index = index + 1
                    if message[index] == ';':
                        break
                    break
                
finally:
    ser.close()