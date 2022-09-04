from email import message
import os
from flask import request
from utils.auth_handler import AuthHandler
from utils.mqtt_handler import connect_mqtt, publish_mqtt

auth = AuthHandler()

# @auth.auth_wrapper
def index():
   pass

def set_mqtt():
   client_id = f'python-mqtt-{os.urandom(32)}'
   topic = ''
   message = ''
   host = 'xsanjaya.me'
   port = 1883
   username = 'xsanjaya'
   password = 'jancokasu'

   mqtt_client = connect_mqtt(client_id, username, password, host, port)
   mqtt_pub    = publish_mqtt((mqtt_client, topic, message ))