from flask import Flask
from flask_migrate import Migrate

from models import db
from routes.api import api_route
from routes.api.UserRoute import user_route
from routes.api.AuthRoute import auth_route
from routes.api.MqttRoute import mqtt_route

from routes.web import web_route
from config import AppConfig

from swagger_ui import api_doc

app = Flask(__name__)
app.config.from_object(AppConfig)

db.init_app(app)
migrate = Migrate(app, db)

api_doc(app, config_path='utils/doc.yaml', url_prefix='/api/doc', title='API doc', editor=True)


### ROUTE API ###
app.register_blueprint(api_route, url_prefix='/api')
app.register_blueprint(auth_route, url_prefix='/api/auth')
app.register_blueprint(user_route, url_prefix='/api/users')
app.register_blueprint(mqtt_route, url_prefix='/api/mqtt')


### ROUTE WEB ###
app.register_blueprint(web_route, url_prefix='/')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
