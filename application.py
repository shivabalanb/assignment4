from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return os.environ.get("MY_ENV_VAR", "")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
