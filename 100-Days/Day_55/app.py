from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Universe!"

@app.route('/greet')
def greeting():
    return "Good day!"