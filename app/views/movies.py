from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        all_movies = movie_service.get_all(director_id, genre_id, year)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = movie_service.get_one(uid)
            return movie_schema.dump(movie), 200

        except Exception:
            return "Not found", 404

    def put(self, uid):
        req_json = request.json
        req_json["id"] = uid
        movie_service.update(req_json)

        return "", 204

    def patch(self, uid):
        req_json = request.json
        req_json["id"] = uid
        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, uid):
        movie_service.delete(uid)

        return "", 204
