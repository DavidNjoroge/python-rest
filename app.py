
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify


db_connect =create_engine('sqlite:///database_epl.db')
app=Flask(__name__)
api=Api(app)

class Teams(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select team,position,points,goals from data") # This line performs query and returns json result
        results = {'teams': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} # Fetches first column that is Employee ID
        return jsonify(results)

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select goals, points, position, from data;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select team,position from data where position =%d "  %int(position))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

# api.add_resource('/quote', QuoteResource())
api.add_resource(Teams, '/teams') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/teams/<position>') # Route_3


if __name__ == '__main__':
     app.run(debug=True)
