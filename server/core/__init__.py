from flask import Flask
from flask import send_file
from services.postgres import postgres
from core.config.base_config import BaseConfig

# create application
app = Flask(__name__)

# configure application
app.config.from_object(BaseConfig)

# connect to services
postgres.app = app
postgres.init_app(app)


# angular application
@app.route('/')
def home_page():
    return send_file('../../client/core/views/client.html')


# connect blueprints
from identity import blueprint
app.register_blueprint(blueprint, url_prefix='/api')

# connect application CLI
from core.commands import commands
