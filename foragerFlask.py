from flask import Flask, jsonify, request
from pymongo import MongoClient
import json 
from bson import json_util

app = Flask(__name__)

# client = MongoClient("mongodb+srv://brendanhughes:LeoDalton1@foragercluster.29jmm.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
# mydb = client["foodData"]
# mycol = mydb["recipes"]


@app.route('/')
def main():
		return "Successfully connected."

@app.route('/home/<string:conditionName>/<int:conditionParams>/<int:conditionParams2>')
def home(conditionName,conditionParams,conditionParams2):
		query = {conditionName:{"$gt":conditionParams,"$lt":conditionParams2}}
		recipe = list(mycol.find(query).limit(2))
		string = json.dumps(recipe,default=json_util.default)
		return string

