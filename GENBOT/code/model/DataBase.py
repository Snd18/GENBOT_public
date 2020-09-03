class DataBase():

    def __init__(self, name, table):
        self.name = name
        self.table = table

    @property
    def name(self):
        return self.__name

    @property
    def table(self):
        return self.__table

    @name.setter
    def name(self, name):
        self.__name = name

    @table.setter
    def table(self, table):
        self.__table = table
