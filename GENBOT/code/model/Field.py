class Field():

    def __init__(self, name, synonyms, order, values, entity_meta, db_meta):
        self.name = name
        self.synonyms = synonyms
        self.order = order
        self.values = values
        self.entity_meta = entity_meta
        self.db_meta = db_meta
        #self.entity_alias = self.tablename + '_' + self.name

    @property
    def entity_alias(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @property
    def synonyms(self):
        return self.__synonyms

    @property
    def order(self):
        return self.__order

    @property
    def values(self):
        return self.__values

    @property
    def entity_meta(self):
        return self.__entity_meta

    @property
    def db_meta(self):
        return self.__db_meta

    @name.setter
    def name(self, name):
        self.__name = name

    @synonyms.setter
    def synonyms(self, synonyms):
        self.__synonyms = synonyms

    @order.setter
    def order(self, order):
        self.__order = order

    @values.setter
    def values(self, values):
        self.__values = values

    @entity_meta.setter
    def entity_meta(self, entity_meta):
        if entity_meta == 'None':
            self.__entity_meta = '@' + self.__name
        else:
            self.__entity_meta = '@' + entity_meta

    @db_meta.setter
    def db_meta(self, db_meta):
        self.__db_meta = db_meta
