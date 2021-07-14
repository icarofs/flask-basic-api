from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify("Hello World")


app.run(port=5000)
