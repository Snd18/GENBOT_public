class Properties():

    def __init__(self, info_map, training_phrases):
        self.info_map = info_map
        self.training_phrases = training_phrases

    @property
    def info_map(self):
        return self.__info_map

    @property
    def training_phrases(self):
        return self.__training_phrases

    @info_map.setter
    def info_map(self, info_map):
        self.__info_map = info_map

    @training_phrases.setter
    def training_phrases(self, training_phrases):
        self.__training_phrases = training_phrases
