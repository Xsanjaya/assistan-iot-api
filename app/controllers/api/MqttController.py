import os, datetime
from flask import request, make_response, json
from utils.auth_handler import AuthHandler
from utils.mqtt_handler import connect_mqtt, publish_mqtt

auth = AuthHandler()

# @auth.auth_wrapper
def index():
   resp = {
            "success" : True,
            "error"   : None,
            "message" : "",
            "data"    : []
      }
   return make_response(json.dumps(resp), 200)

def set_mqtt():
   req = request.json
   client_id = f'python-mqtt-{os.urandom(32)}'
   topic = 'hometech'
   message = req['queryResult']['queryText']
   host = 'xsanjaya.me'
   port = 1883
   username = 'xsanjaya'
   password = 'jancokasu'
   try:

      mqtt_client = connect_mqtt(client_id, username, password, host, port)
      mqtt_pub    = publish_mqtt(mqtt_client, topic, message )
      
      resp = {
               "success" : True,
               "error"   : None,
               "message" : "",
               "data"    : [mqtt_pub]
         }
      resp_code = 200
   
   except Exception as err:
      resp = {
               "success" : False,
               "error"   : str(err),
               "message" : "",
               "data"    : []
         }
      resp_code = 403
   return make_response(json.dumps(resp), resp_code)

def assistant():
   req = request.json
   # resp_param = req['queryResult']['parameters']
   # client_id = f'python-mqtt-{os.urandom(32)}'
   # message = resp_param
   # topic = 'hometech'
   # host = 'xsanjaya.me'
   # port = 1883
   # username = 'xsanjaya'
   # password = 'jancokasu'

   # mqtt_client = connect_mqtt(client_id, username, password, host, port)
   # mqtt_pub    = publish_mqtt(mqtt_client, topic, str(message) )

   resp_code = 200
   print(f'\n{datetime.datetime.now()}\n', json.dumps(req['session']['params']),f'\n\n' )
   return make_response(req, resp_code)