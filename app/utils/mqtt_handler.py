from http import client
from unittest import result
from paho.mqtt import client as mqtt_client


def connect_mqtt(client_id, username, password, host, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(host, port)
    return client


def subscribe(client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def publish_mqtt(client, topic, message):
    pub = client.publish(topic, message)
    result = message
    # try:
    #     pub = client.publish(topic, message)
    #     result = {
    #         "success" : True,
    #         "topic" : topic,
    #         "message" : message
    #     }
    # except Exception as err:
    #     result = {
    #         "success" : False,
    #         "topic" : topic,
    #         "message" : message
    #     }
    return result
