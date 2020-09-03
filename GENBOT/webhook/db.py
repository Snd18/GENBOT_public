import mysql.connector as sql


class DB:

    def __init__(self, host, user, password, database, port):
        # inicializar bd mysql
        self.db = sql.connect(host = host,
                            user = user,
                            password = password,
                            database = database,
                            port=port)
        # cursor para usarlo en queries siguientes
        self.cur = self.db.cursor()

    # obtener todas las filas de appointments
    def select(self, select):
        self.cur.execute(select)
        try:
            result = [x[0].encode('latin1') for x in self.cur.fetchall()]
            if result == []:
                result = 'No results found'
            return result
        except:
            return "Database error"

    def executeQuery(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    # cerrar conexion a la bd y cursor. Hacer los cambios permanentes
    def close(self):
        if (self.db):
            self.cur.close()
            self.db.close()
