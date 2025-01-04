from flask import Flask

app = Flask(__name__)

@app.route("/info")
def test():
    return "This test was done by Harshit Sharma"

app.run(host='0.0.0.0')
