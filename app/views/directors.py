from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema


director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)

        return "", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        try:
            director = director_service.get_one(uid)
            return director_schema.dump(director), 200

        except Exception:
            return "Not found", 404

    def put(self, uid):
        req_json = request.json
        req_json["id"] = uid
        director_service.update(req_json)

        return "", 204

    def patch(self, uid):
        req_json = request.json
        req_json["id"] = uid
        director_service.update_partial(req_json)

        return "", 204

    def delete(self, uid):
        director_service.delete(uid)

        return "", 204
