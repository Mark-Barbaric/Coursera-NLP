from flask_restful import Api, Resource

class UserAPI(Resource):
    users = []
    id = 0
    def get(self, name):
        for user in self.users:
            if user['name'] == name:
                return user
            
    def post(self, name):
        user = {'name' : name, 'id' : self.id}
        self.id += 1
        self.users.append(user)
        return user