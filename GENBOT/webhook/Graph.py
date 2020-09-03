import db
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


class Graph():

    PATH = '../images/'
    SERVERIMG = 'https://661dcce0.ngrok.io/images?id='

    def __init__(self, fields, table, database, type, id):
        self.fields = fields
        self.table = table
        self.database = database
        self.type = type
        self.id = id

    @property
    def fields(self):
        return self.__fields

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

    @fields.setter
    def fields(self, fields):
        self.__fields = fields

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

    def getGraph(self):
        query = self.getGraphQuery()
        fullPathImage = self.PATH + self.id + '.png'
        try:
            # conectar con la bd
            con = db.DB("localhost", "root", "", self.database, 3306)
            result = con.executeQuery(query)
            x = []
            for i in range(len(result[0])):
                xx = [item[i] for item in result]
                x.append(xx)
            if self.type == 'line graph (X vs Y)':
                plt.plot(x[0], x[1])
                plt.xlabel(self.fields[0])
                plt.ylabel(self.fields[1])
            elif self.type == 'scatter plot (X vs Y)':
                plt.plot(x[0], x[1], 'ro')
                plt.xlabel(self.fields[0])
                plt.ylabel(self.fields[1])
            elif self.type == 'line graph (series)':
                for i in range(len(x)):
                    plt.plot(x[i], label=self.fields[i])
                    plt.xlabel('i')
                    plt.ylabel('values')
            elif self.type == 'scatter plot (series)':
                color = ['red', 'blue']
                for i in range(len(x)):
                    plt.plot(x[i], 'ro', color=color[i], label=self.fields[i])
                    plt.xlabel('i')
                    plt.ylabel('values')
            plt.legend(loc='upper left')
            plt.savefig(fullPathImage)
            plt.close()
            return id
        except Exception as e:
            raise e

        finally:
            # si la conexion se ha creado --> cerrarla
            if (con):
                con.close()

    def getGraphQuery(self):
        fields = ''
        groupBy = ''
        for i, field in enumerate(self.fields):
            fields = fields + field + ', '
            groupBy = groupBy + str(i + 1) + ','
        fields = fields[:-2]
        groupBy = groupBy[:-1]
        query = 'select fields from table group by groupBy'
        query = query.replace('fields', fields)
        query = query.replace('table', self.table)
        query = query.replace('groupBy', groupBy)
        print(query)
        return query
