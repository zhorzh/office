from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/')
def home_page():
    return send_file('../../client/core/views/client.html')
