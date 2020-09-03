import db
import numpy as np
import matplotlib.pyplot as plt

class Pie():

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

    def getPie(self):
        query = self.getPieQuery()
        fullPathImage = self.PATH + self.id + '.png'
        try:
            # conectar con la bd
            con = db.DB("localhost", "root", "", self.database, 3306)
            # get result from db
            result = con.executeQuery(query)
            # transform the results
            word = np.array([item[0] for item in result])
            frequency = np.array([item[1] for item in result])
            # to calculate the porcentages
            totalSum = np.sum(frequency)
            prct = (frequency*100) / totalSum
            # pie chart
            labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(word, prct)]
            fig1, ax1 = plt.pie(prct, shadow=True, startangle=90)
            # order labels by frecuency
            fig1, labels, dummy = zip(*sorted(zip(fig1, labels, frequency), key=lambda x: x[2], reverse=True))
            #ax1.axis('equal')
            plt.legend(fig1, labels, loc='center left', bbox_to_anchor=(-0.1, 1.), fontsize=8)
            #plt.legend()
            plt.savefig(fullPathImage, bbox_inches='tight')
            plt.close()
        except Exception as e:
            print(e)
            raise e

        finally:
            # si la conexion se ha creado --> cerrarla
            if (con):
                con.close()


    def getPieQuery(self):
        query = 'select field, count(field) from table group by field'
        query = query.replace('field', self.field)
        query = query.replace('table', self.table)
        return query
