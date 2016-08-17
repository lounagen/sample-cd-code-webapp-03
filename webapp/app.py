from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World in webapp-01!"

if __name__ == "__main__":
    app.run()

