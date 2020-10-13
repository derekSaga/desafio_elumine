from flask_restful import Resource
from flask import make_response
from app.service.user_service import get_user_paper
from app.schema.user_schema import UserCategory
from app import api


class UserList(Resource):
    def get(self):
        users = get_user_paper()
        uc = UserCategory(many=True)
        return make_response(uc.jsonify(users), 200)


api.add_resource(UserList, "/v1/user")
