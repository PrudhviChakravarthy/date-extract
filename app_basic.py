import os
from flask import Flask, render_template, request
from Date_extractor import date_find, base_converter
import base64


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return "ok"

@app.route('/extract_date', methods = ['POST'])
def user():
    x = request.form['string']
    #return str(len(x))
    base_converter(x)
    x = date_find("image.png")
    if  x == None :
        return {"Date" : x}
    else:
        return {"Date" : x}
    #return "done"

if __name__ == "__main__":
    app.run(port=4555, debug=True)