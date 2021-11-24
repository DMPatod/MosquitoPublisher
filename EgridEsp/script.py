import serial
from paho.mqtt import client as mqtt_client

PORT = '/dev/ttyUSB0'

ser = serial.Serial(port=PORT,baudrate=115200,timeout=1)

try:
    while True:
        message = ser.readline().decode()
        print(f'recv {message}')
finally:
    ser.close()

def connect_mosquitto():
    def on_connect(client, userdata, flagas, rc):
        if rc == 0:
            print("Connected to Mosquitto Broker!")
        else:
            print("Connect failed, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client