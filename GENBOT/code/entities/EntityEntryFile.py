from utils import utils


# [nameEntity]_entries_en.json content
class EntityEntryFile():

    path = "../outputs/v4/entities/"

    def __init__(self, name, entrys):
        self.name = name
        self.entrys = entrys

    @property
    def filepath(self):
        return self.path + self.__name + '_entries_en.json'

    @property
    def name(self):
        return self.__name

    @property
    def values(self):
        return self.__values

    @name.setter
    def name(self, name):
        self.__name = name

    @values.setter
    def values(self, values):
        self.__values = values

    def writeToFile(self):
        utils.writeToFile(self.entrys, self.filepath)
