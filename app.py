from flask import Flask,jsonify,Response
import boto3
from xml.etree.ElementTree import parse,tostring,fromstring
import os

app=Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message":"This is the success message"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000,debug=False)