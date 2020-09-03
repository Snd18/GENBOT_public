

class Sentence():

    # to represent one training phrase

    def __init__(self, id, data):
        self.id = id
        self.data = data

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def sentence(self):
        sentence = {
            "id": self.id,
            "data": self.data,
            "istemplate": False,
            "count": 0
        }
        return sentence

    @id.setter
    def id(self, id):
        self.__id = id

    @data.setter
    def data(self, data):
        self.__data = data
