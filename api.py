from flask import Flask,jsonify,Response
import boto3
from xml.etree.ElementTree import parse,tostring,fromstring
import os
from dotenv import load_dotenv
load_dotenv()

s3=boto3.client("s3",aws_access_key_id=os.getenv("AWS_SECRET_ID"),aws_secret_access_key="T8FfsJfclVaK+wiFtL8Fi6TQWS9p86q2IiSKYS0Q")
app=Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message":"This is the success message"})

def get_data_from_s3(bucket_name, key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        data = response['Body'].read().decode("utf-8")
        return data
    except Exception as e:
        raise e

@app.route('/xml_data')
def get_data():
    xml_data = get_data_from_s3("stackoverflowquery", "stack_overflow_data/data.xml")
    root = fromstring(xml_data)
    xml_string = tostring(root, encoding="unicode")
    return Response(xml_string, mimetype="text/xml")



if __name__=="__main__":
    app.run(host="localhost",port=4000,debug=True)