class GenreService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")

        genre = self.get_one(uid)

        genre.name = data.get("name")

        self.dao.update(genre)

    def update_partial(self, data):
        uid = data.get("id")

        genre = self.get_one(uid)

        if "name" in data:
            genre.name = data.get("name")

        self.dao.update(genre)

    def delete(self, uid):
        self.dao.delete(uid)
