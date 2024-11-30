from flask import Flask, jsonify, request

app = Flask(__name__)

#create a home route. for now it will display hello world.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"