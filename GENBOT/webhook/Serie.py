import db
import matplotlib.pyplot as plt


class Serie():

    PATH = '../images/'
    SERVERIMG = 'https://661dcce0.ngrok.io/images?id='

    def __init__(self, field, table, database, type, id):
        self.field = field
        self.table = table
        self.database = database
        self.type = type
        self.id = id

    @property
    def field(self):
        return self.__field

    @property
    def table(self):
        return self.__table

    @property
    def database(self):
        return self.__database

    @property
    def type(self):
        return self.__type

    @property
    def id(self):
        return self.__id

    @field.setter
    def field(self, field):
        self.__field = field

    @table.setter
    def table(self, table):
        self.__table = table

    @database.setter
    def database(self, database):
        self.__database = database

    @type.setter
    def type(self, type):
        self.__type = type

    @id.setter
    def id(self, id):
        self.__id = id

    def getSerie(self):
        query = self.getSerieQuery()
        print('he')
        fullPathImage = self.PATH + self.id + '.png'
        try:
            # conectar con la bd
            con = db.DB("localhost", "root", "", self.database, 3306)
            result = con.executeQuery(query)
            x = [item[0] for item in result]
            if self.type == 'line graph':
                plt.plot(x)
            else:
                plt.plot(x, 'ro')
            plt.xlabel('i')
            plt.ylabel(self.field)
            plt.savefig(fullPathImage)
            plt.close()
        except Exception as e:
            raise e

        finally:
            # si la conexion se ha creado --> cerrarla
            if (con):
                con.close()


    def getSerieQuery(self):
        query = 'select field from table group by 1'
        query = query.replace('field', self.field)
        query = query.replace('table', self.table)
        return query
