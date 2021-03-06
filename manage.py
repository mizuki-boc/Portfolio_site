# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/research")
def research():
    return render_template("research.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888, threaded=True)