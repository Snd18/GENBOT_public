class Table():

    dir_local = '../data/'
    header = 0
    deli = ';'

    def __init__(self, name, csv_url, fields):
        self.name = name
        self.csv_url = csv_url
        self.fields = fields

    @property
    def name(self):
        return self.__name

    @property
    def fields(self):
        return self.__fields

    @property
    def csv_url(self):
        return self.__csv_url

    @property
    def csv_local(self):
        return self.dir_local + self.__name + '.csv'

    @property
    def headers(self):
        return self.header

    @property
    def delimiter(self):
        return self.deli

    @name.setter
    def name(self, name):
        self.__name = name

    @fields.setter
    def fields(self, fields):
        self.__fields = fields

    @csv_url.setter
    def csv_url(self, csv_url):
        self.__csv_url = csv_url
