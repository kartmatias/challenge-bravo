from flask import Flask, escape, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import requests

db_connect = create_engine('sqlite:///bravo.db')
app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    name = request.args.get("name", "API")
    return f'Bravo Currency Conversion , {escape(name)}!'


class UpdateTables(Resource):
    def get(self):
        response = requests.get('https://api.github.com')
        if response.status_code == 200:
            result = {
                "data": {
                    "message": "SUCESS"
                }
            }
        elif response.status_code == 404:
            result = {
                "data": {
                    "message": "NOT FOUND"
                }
            }
        return jsonify(result)


class CurrencyConverter(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("Select * from CurrencyConverter")
        return {'Price': [i[0] for i in query.cursor.fetchall()]}


class CurrencyList(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("Select * from CurrencyList")
        result = {'data': [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        return jsonify(result)


api.add_resource(CurrencyConverter, '/price')
api.add_resource(CurrencyList, '/list')
api.add_resource(UpdateTables, '/update')

if __name__ == '__main__':
    app.run(port='5052',
            debug=True)
