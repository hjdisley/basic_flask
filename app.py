from flask import Flask

app = Flask(__name__)

@app.route("/raspberrypi")
def hello_world():
    return "<p>Running on Pi</p>"