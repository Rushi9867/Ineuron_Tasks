from flask import Flask,request,jsonify
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps,loads

app = Flask(__name__)

@app.route('/insert',methods=["GET","POST"])
def insert():
    if request.method == 'POST':
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["FlASGO"]
        collection = db["Flask"]
        id = request.json['Id']
        name = request.json['Name']
        age = request.json['Age']
        salary = request.json['Salary']
        record = {"Id":id,"Name":name,"Age":age,"Salary":salary}
        c = collection.insert_one(record)
        c1 = c.inserted_id
        return jsonify((str(c1)))

@app.route('/update',methods=['PUT','POST'])
def upadte():
    if request.method == 'PUT':
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["FlASGO"]
        collection = db["Flask"]
        id = request.json['Id']
        name = request.json["Name"]
        age = request.json["Age"]
        up = {"Name":name,"Age":age}
        collection.update_many({"Id":id},{"$set":up})
        return "Update Successfully"
''' 
{
    "Id":101,
    "Name":"Kamal",
    "Age":24
}
'''
@app.route('/delete',methods=['PUT','DELETE'])
def delete():
    if request.method == 'DELETE':
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["FlASGO"]
        collection = db["Flask"]
        id = request.json['Id']
        d1 = collection.delete_one({'Id':id})
        return 'DELETE Successfully'

@app.route('/fetch',methods=['GET','POST'])
def fetch():
    if request.method == 'GET':
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["FlASGO"]
        collection = db["Flask"]
        f1 = collection.find()
        data = dumps(list(f1))
        return data
        
if __name__ == '__main__':
    app.run(debug=True)
