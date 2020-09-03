from utils import utils


class UsersaysIntent():

    # [nameIntent]_usersays_en.json content

    path = "../outputs/v4/intents/"

    def __init__(self, name, json):
        self.name = name
        self.json = json

    @property
    def name(self):
        return self.__name

    @property
    def json(self):
        return self.__json

    @name.setter
    def name(self, name):
        self.__name = name

    @json.setter
    def json(self, json):
        self.__json = json

    def writeToFile(self):
        utils.writeToFile(self.json, self.filepath + self.name + '_usersays_en.json')
