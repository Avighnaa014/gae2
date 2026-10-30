from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World.\n This web page is launched using Google App Engine."
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
