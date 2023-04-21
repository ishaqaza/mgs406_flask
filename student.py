from flask import FLask, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello <b>World</b>"

if __name__ == "__main__":
    app.run()



