import mysql.connector as sql
from db import dbutils


class DB():

    def __init__(self, host, user, password, port, db):
        '''
        Init db
        '''
        self.db = db
        self.con = sql.connect(host = host,
                            user = user,
                            password = password,
                            port=port, allow_local_infile=True)
        # for next querys
        self.cur = self.con.cursor()

    @property
    def db(self):
        return self.__db

    @property
    def con(self):
        return self.__con

    @property
    def cur(self):
        return self.__cur

    @db.setter
    def db(self, db):
        self.__db = db

    @con.setter
    def con(self, con):
        self.__con = con

    @cur.setter
    def cur(self, cur):
        self.__cur = cur

    # create db
    def createDB(self):
        '''
        Create db with name.
        '''
        sql = "CREATE DATABASE IF NOT EXISTS " + self.db.name
        self.cur.execute(sql)

    def createTable(self):
        '''
        Create table on db.
        '''
        # enter db
        #self.cur.execute("USE " + dbname)
        sql = "USE " + self.db.name
        self.cur.execute(sql)

        # drop table if exists
        self.dropTable(self.db.name, self.db.table.name)
        # create string to create table
        strCreate = dbutils.queryCreateTable(self.db.table)
        # execute create table
        self.cur.execute(strCreate)

    def dropTable(self, dbname, tablename):
        '''
        Drop a given table if exists.
        '''
        sql = "USE " + dbname
        self.cur.execute(sql)

        # create string to drop table
        sql = "DROP TABLE IF EXISTS " + tablename
        # execute drop table
        self.cur.execute(sql)

    def populateTable(self):
        '''
        Populate a given table with csv.
        '''
        # to show warning instead of error when a field is empty
        self.cur.execute('SET sql_mode = ""')
        populate = "LOAD DATA LOCAL INFILE '" + self.db.table.csv_local \
        + "' REPLACE INTO TABLE " + self.db.table.name + ' '\
        + "CHARACTER SET latin1" \
        + " FIELDS TERMINATED BY '" + self.db.table.delimiter + "' OPTIONALLY ENCLOSED BY '" + '"' \
        + "' LINES TERMINATED BY '\\n' IGNORE 1 ROWS ;"
        self.cur.execute(populate)
        # to avoid error of cursor sync
        self.cur.close()
        #self.db.cursor()

    # cerrar conexion a la bd y cursor. Hacer los cambios permanentes
    def close(self):
        '''
        Close db conection and cursor and make a commit.
        '''
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.commit()
            self.con.close()
