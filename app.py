#setting up Flask.
from flask import Flask, render_template, url_for, session, redirect, request
from yahoo_finance import Share
import requests
app = Flask(__name__)

# Defining Route
@app.route('/')
def home():
    return "This is the home page."

@app.route("/ticker/<tickervar>")
def lookupStock(tickervar):
    tickervar = tickervar.upper()
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(tickervar)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == str(tickervar):
            return render_template("stockchartexample.html", stocktickername=tickervar)
        else:
            return "Sorry, no such stock exists."
# Added Run Option.
if __name__ == '__main__':
    app.run()
