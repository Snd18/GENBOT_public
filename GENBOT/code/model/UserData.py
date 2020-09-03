
class UserData():

    def __init__(self, username, db, properties):
        self.username = username
        self.db = db
        self.properties = properties

    @property
    def username(self):
        return self.__username

    @property
    def db(self):
        return self.__db

    @property
    def properties(self):
        return self.__properties

    @username.setter
    def username(self, username):
        self.__username = username

    @db.setter
    def db(self, db):
        self.__db = db

    @properties.setter
    def properties(self, properties):
        self.__properties = properties
