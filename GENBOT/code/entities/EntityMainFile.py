from utils import utils


# [nameEntity].json content
class EntityMainFile():

    path = "../outputs/v4/entities/"

    def __init__(self, id, name, automatedExpansion):
        self.id = id
        self.name = name
        self.automatedExpansion = automatedExpansion

    @property
    def entity(self):
        e = {
            'id': self.__id,
            'name': self.__name,
            'isOverridable': True,
            'isEnum': False,
            'isRegexp': False,
            'automatedExpansion': self.__automatedExpansion,
            'allowFuzzyExtraction': False
        }
        return e

    @property
    def filepath(self):
        return self.path + self.__name + '.json'

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def automatedExpansion(self):
        return self.__automatedExpansion

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @automatedExpansion.setter
    def automatedExpansion(self, automatedExpansion):
        self.__automatedExpansion = automatedExpansion

    def writeToFile(self):
        utils.writeToFile(self.entity, self.filepath)
