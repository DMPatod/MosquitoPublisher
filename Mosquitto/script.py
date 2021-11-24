from paho.mqtt import client as mqtt

publisher = mqtt.Client("publish")
publisher.connect(host="192.168.1.102", port=1883, keepalive=60, bind_address="")

topic = "sensorA/current"
message = "hello world"

publisher.publish(topic,message)
print("Published: " + message + " to topic + " + topic)