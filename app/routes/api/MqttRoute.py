from flask import Blueprint
from controllers.api.MqttController import index, set_mqtt

mqtt_route = Blueprint('mqtt_route', __name__)

mqtt_route.route('/', methods=['POST'])(index)
mqtt_route.route('/', methods=['POST'])(set_mqtt)