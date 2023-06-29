from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/dec")
def decorator():
    return "<h2>Python is a lot</h2>"




@app.route("/cook")
def cook():
    return "<h1>Let him cook</h1>"

if __name__ == "__main__":
    app.run()
