from db import DB as dbCon


def queryCreateTable(table):
    '''
    Create string to execute on db and create a table.
    '''
    str = " create table " + table.name + " ( "
    for field in table.fields:
        str = str + ' ' + field.name + ' ' + field.db_meta + ','
    # remove last comma
    str = str[:-1]
    str = str + ' ) character set latin1 collate latin1_general_ci;'
    return str


def createDB(db):
    # conectar con la bd
    # TODO crear db
    con = None

    try:
        #con = dbExecute.DB("localhost", "root", "", "botSQL", 3306)
        con = dbCon.DB("localhost", "root", "", 3306, db)
        con.createDB()
        con.createTable()
        con.populateTable()
    except Exception as e:
        print("Can't create db")
        raise
    finally:
        # si la conexion se ha creado --> cerrarla
        if (con):
            con.close()
