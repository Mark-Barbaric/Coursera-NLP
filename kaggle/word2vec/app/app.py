from flask import Flask
from flask_restful import Api, Resource
from users import UserAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(UserAPI, '/users/<string:name>', endpoint = 'user')

if __name__ == "__main__":
  app.run()