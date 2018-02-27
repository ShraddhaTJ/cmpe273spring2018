from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
#variable declare
id=1
dic=[]

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    global id
    
    name=request.form["name"]
    dic.append({"id":id,"name":name})
    id_copy=id
    id+=1
    return jsonify({"id":id_copy,"name":name})


@app.route('/users/1',methods=['GET'])
def get_users():
    return jsonify(dic[0])

@app.route('/users/1',methods=['DELETE'])
def delete_users():
    dic.pop(0)
    return ('',204)
