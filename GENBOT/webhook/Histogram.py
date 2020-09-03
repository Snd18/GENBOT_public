import db
import numpy as np
import matplotlib.pyplot as plt


class Histogram():

    PATH = '../images/'
    SERVERIMG = 'https://661dcce0.ngrok.io/images?id='

    def __init__(self, field, table, database, id):
        self.field = field
        self.table = table
        self.database = database
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

    @id.setter
    def id(self, id):
        self.__id = id

    def getHistogram(self):
        query = self.getHistogramQuery()
        fullPathImage = self.PATH + self.id + '.png'
        try:
            # conectar con la bd
            con = db.DB("localhost", "root", "", self.database, 3306)
            result = con.executeQuery(query)
            word = [item[0] for item in result]
            frequency = [item[1] for item in result]
            indices = np.arange(len(result))
            plt.bar(indices, frequency, color='r')
            #plt.xlim(0.3, 0.4)
            #plt.locator_params(axis='y', nbins=6)
            #plt.locator_params(axis='x', nbins=10)
            plt.xticks(indices, word, rotation='vertical')
            plt.tight_layout()
            #plt.show()
            plt.savefig(fullPathImage)
            plt.close()
            print('en el grafico')
        except Exception as e:
            raise e

        finally:
            # si la conexion se ha creado --> cerrarla
            if (con):
                con.close()


    def getHistogramQuery(self):
        query = 'select field, count(field) from table group by field'
        query = query.replace('field', self.field)
        query = query.replace('table', self.table)
        return query
