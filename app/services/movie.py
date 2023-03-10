class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self, director, genre, year):
        if director is not None:
            return self.dao.get_by_director(director)
        elif genre is not None:
            return self.dao.get_by_genre(genre)
        elif year is not None:
            return self.dao.get_by_year(year)
        else:
            return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")

        movie = self.get_one(uid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")

        self.dao.update(movie)

    def update_partial(self, data):
        uid = data.get("id")

        movie = self.get_one(uid)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")

        self.dao.update(movie)

    def delete(self, uid):
        self.dao.delete(uid)
