from flask import Flask
from flask import send_file
from services.postgres import postgres
from core.config.base_config import BaseConfig

app = Flask(__name__)

app.config.from_object(BaseConfig)

postgres.app = app
postgres.init_app(app)


@app.route('/')
def home_page():
    return send_file('../../client/core/views/client.html')
