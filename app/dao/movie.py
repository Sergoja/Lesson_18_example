from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, uid):
        movie = self.get_one(uid)

        self.session.delete(movie)
        self.session.commit()

    def get_by_director(self, uid):
        return self.session.query(Movie).filter(Movie.director_id == uid).all()

    def get_by_genre(self, uid):
        return self.session.query(Movie).filter(Movie.genre_id == uid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()
