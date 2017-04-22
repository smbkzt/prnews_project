from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash

from users.models import Users, db, UsersSchema

users = Blueprint('users', __name__)
api = Api(users)
schema = UsersSchema()


class UserFilter(Resource):
    def get(self, some_filter):
        dictionary_of_filters = {}
        split_filters_by_coma = str(some_filter).split(',')
        create_filter = []

        # Создаем словарь "фильтр: значение"
        for filter_ in split_filters_by_coma:
            dictionary_of_filters[
                filter_.split("::")[0]] = str(filter_.split("::")[1]).title()

        for filter_, value in dictionary_of_filters.items():
            create_filter.append("{0}='{1}'".format(filter_, value))

        # Объединяем полученные выше фильтры с оператором AND
        joined_filters = " AND ".join(create_filter)

        found_users = Users.query.filter(joined_filters)
        dumped_result = schema.dump(found_users, many=True).data

        return dumped_result

    def post(self):
        pass


class GetAllUsers(Resource):
    def get(self):
        all_users = Users.query.all()
        result = schema.dump(all_users, many=True).data
        return result

    def post(self):
        raw_dict = request.get_json(force=True)
        user_dict = raw_dict['data']['attributes']
        try:
            schema.validate(user_dict)
            user = Users(**user_dict)
            user.add(user)
            query = Users.query.get(user.id)
            results = schema.dump(query).data
            return results, 201

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp


class UsersUpdate(Resource):
    def get(self, id):
        user_query = Users.query.get_or_404(id)
        result = schema.dump(user_query).data
        return result

    def patch(self, id):
        user = Users.query.get_or_404(id)
        get_request = request.get_json(force=True)

        try:
            schema.validate(get_request)
            get_user_data = get_request['data']['attributes']
            for field_name, field_value in get_user_data.items():
                if field_name == 'password':
                    field_value = generate_password_hash(field_value)
                setattr(user, field_name, field_value)
            user.update()
            return self.get(id)

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 401
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        get_user = Users.query.get_or_404(id)
        try:
            get_user.delete(get_user)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp


api.add_resource(GetAllUsers, '/')
api.add_resource(UsersUpdate, '/<int:id>')
api.add_resource(UserFilter, '/filter=<string:some_filter>')
