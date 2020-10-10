from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "123q123"

app.config["MONGO_URI"] = "mongodb://localhost:27017/zooPilot"

mongo = PyMongo(app)
@app.route('/')
def home():
    #resp = "<center><h1>Welcome to <i>zooPilot</i></h1></center>"
    return render_template("index.html")

"""
    Manage Rooms: 
        * Some Queries
"""
@app.route('/rooms')
def rooms():
    rooms = mongo.db.rooms.find()
    resp = dumps(rooms)
    return resp
@app.route('/rooms/meetings/topics')
def getMeetingsTopic():
    rooms = mongo.db.rooms.distinct("meetings.topic")
    resp = dumps(rooms)
    return resp

@app.route('/meeting/<topic>')
def findMeetingByTopic(topic):
    meeting = mongo.db.rooms.find_one({'meetings.topic': topic})
    resp = dumps(meeting)
    return resp


@app.route('/roomAdmin')
def getRoomAdmin():
    rooms = mongo.db.rooms.aggregate([
  {
     '$lookup':
       {
         'from': "users",
         'localField': "meetings.participants.$id",
         'foreignField': "_id",
         'as': "meetings.participants"
       }
  },
   {
      '$lookup':
         {
            'from': "users",
            'localField': "userAdmin.$id",
            'foreignField': "_id",
            'as': "userAdmin"
        }
   },
   
   {
       '$project':
           { "userAdmin.dateTime" : 0 , "userAdmin.language" : 0, "userAdmin.capacity" : 0}
    }
])
    resp = dumps(rooms)
    return resp


    

"""
    Manage Users: 
        * View users, delete a user, update user and create users
"""
@app.route('/users')
def users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp

@app.route('/user/<email>')
def user(email):
    user = mongo.db.users.find_one({'Email': email})
    resp = dumps(user)
    return resp

@app.route('/delete/<email>', methods=['DELETE'])
def deleteUser(email):
    mongo.db.users.delete_one({'Email': email})
    resp = jsonify("User deleted Successfully")
    resp.status_code = 200
    return resp


@app.route('/add', methods=['POST'])
def addUser():
    _json = request.json
    _PMI = _json['PMI']
    _Email = _json['Email']
    _password = _json['password']
    _hostKey = _json['hostKey']
    _userType = _json['userType']
    _capacity = _json['capacity']
    _language = _json['language']
    #_dateTime = _json[{_json['dateFormat'], _json['timeFormat'], _json['timeZone']}]
    _dateFormat = _json['dateFormat']
    _timeFormat = _json['timeFormat']
    _timeZone  = _json['timeZone']

    if _Email and _password and request.method == 'POST':

        _hashed_password = generate_password_hash(_password)
        mongo.db.users.insert({
            'PMI': _PMI,
            'Email': _Email,
            'password': _password,
            'hostKey': _hostKey,
            'userType': _userType,
            'capacity': _capacity,
            'language': _language,
            'dateTime': {
                'dateFormat': _dateFormat,
                'timeZone': _timeZone,
                'timeFormat': _timeFormat
            }
        })

        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/update/<id>', methods=['PUT'])
def updateUser(id):
    _id = id
    _json = request.json
    _PMI = _json['PMI']
    _Email = _json['Email']
    _password = _json['password']
    _hostKey = _json['hostKey']
    _userType = _json['userType']
    _capacity = _json['capacity']
    _language = _json['language']
    #_dateTime = _json[{_json['dateFormat'], _json['timeFormat'], _json['timeZone']}]
    _dateFormat = _json['dateFormat']
    _timeFormat = _json['timeFormat']
    _timeZone  = _json['timeZone']

    if _Email and _password and request.method == 'PUT':

        _hashed_password = generate_password_hash(_password)
        id = mongo.db.users.update_one({
            '_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
            {'$set':{
            'PMI': _PMI,
            'Email': _Email,
            'password': _password,
            'hostKey': _hostKey,
            'userType': _userType,
            'capacity': _capacity,
            'language': _language,
            'dateTime': {
                'dateFormat': _dateFormat,
                'timeZone': _timeZone,
                'timeFormat': _timeFormat
            }
            }
        })

        resp = jsonify("User updated successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()





@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)

    
    
    
    