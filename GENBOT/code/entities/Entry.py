

# [nameEntity]_entries_en.json content
class Entry():

    path = "../outputs/v4/entities/"

    def __init__(self, value, synonyms):
        self.value = value
        self.synonyms = synonyms

    @property
    def entry(self):
        entry = {
            'value': self.__value,
            'synonyms': self.__synonyms
        }
        return entry

    @property
    def value(self):
        return self.__value

    @property
    def synonyms(self):
        return self.__synonyms

    @value.setter
    def value(self, value):
        self.__value = value

    @synonyms.setter
    def synonyms(self, synonyms):
        self.__synonyms = synonyms
