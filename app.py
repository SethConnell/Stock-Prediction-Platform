#setting up Flask.
from flask import Flask, render_template, url_for, session, redirect, request
app = Flask(__name__)

# Defining Route
@app.route('/')
def home():
    return "This is the home page."

# Added path to view chart.
@app.route("/chart")
def chart():
    return render_template("stockchartexample.html")

# Added path to view info.
@app.route("/stockinfo")
def stockinfo():
    return render_template("stockinfo.html")

# Added Run Option.
if __name__ == '__main__':
    app.run()
