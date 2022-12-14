from flask import Blueprint
from controllers.api.MqttController import index, set_mqtt, assistant

mqtt_route = Blueprint('mqtt_route', __name__)

mqtt_route.route('/', methods=['GET'])(index)
mqtt_route.route('/', methods=['POST'])(set_mqtt)
mqtt_route.route('/assistant', methods=['POST'])(assistant)