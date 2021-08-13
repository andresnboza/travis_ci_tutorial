import os
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

PORT = os.getenv('PORT')

class ServerWorking(Resource):
    def get(self):
        return {'Server': 'working'}


api.add_resource(ServerWorking, '/')


if __name__ == "__main__":
    try:
        print("service_one is working on port " + PORT, flush=True)
        app.run(debug=True, host='0.0.0.0', port=PORT)
    except:
        print(
            "=====> An exception occurred with the server!!!")