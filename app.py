#setting up Flask.
from flask import Flask, render_template, url_for, session, redirect, request
app = Flask(__name__)

# Defining Route
@app.route('/')
def home():
    return "This is the home page."

# Added Run Option.
if __name__ == '__main__':
    app.run()
