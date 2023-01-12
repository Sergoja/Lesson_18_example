class DirectorService:
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

        director = self.get_one(uid)

        director.name = data.get("name")

        self.dao.update(director)

    def update_partial(self, data):
        uid = data.get("id")

        director = self.get_one(uid)

        if "name" in data:
            director.name = data.get("name")

        self.dao.update(director)

    def delete(self, uid):
        self.dao.delete(uid)
