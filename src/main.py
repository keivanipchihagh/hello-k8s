import os
from dotenv import load_dotenv
from flask import Flask, render_template

APP = Flask(__name__)
load_dotenv()


@APP.route("/")
def index():
  return render_template("index.html")



if __name__ == '__main__':
    APP.run(
        host = os.getenv('HOST', '0.0.0.0'),
        port = os.getenv('PORT', 80),
        debug = True
    )