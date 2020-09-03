# importar framework Flask para crear webhook
from flask import Flask
from flask import jsonify
from flask import request
from flask import send_file
import Histogram as histogram
import Request as rqst
import Pie as pie
import Map as map
import Graph as graph
import Serie as serie
import Response as response
import db
import time
import os.path
import threading
import traceback

# intent names
HELP_INTENT = 'Help'
SIMPLEGRAPH_INTENT = 'Ask for simple graph'
COMPLEXGRAPH_INTENT = 'Ask for complex graph'
TYPESIMPLEGRAPH_INTENT = 'Simple graph - type'
TYPECOMPLEXGRAPH_INTENT = 'Complex graph - type'
GETIMAGE_INTENT = 'GetImage'
MAP_INTENT = 'Ask for map'
GETMAPFROMID_INTENT = 'GetMap'

# error codes
DBERRORS = ['Database error', 'No results found', 'There are problems with db. Try later.']

# inicializar Flask
app = Flask(__name__)

defaultEntities = ['phone-number', 'number', 'url', 'date']

www = 'd2b4041f8d50'

# for files
endPointFiles = 'https://'+ www +'.ngrok.io/files?id='
filesPath = '../files/'
FILEROUTE = '/files'
# for images
endPointImages = 'https://'+ www +'.ngrok.io/images?id='
imagesPath = '../images/'
IMAGESROUTE = '/images'
# for maps
endPointMaps = 'https://'+ www +'.ngrok.io/maps?id='
mapsPath = '../maps/'
MAPSROUTE = '/maps'
# for html files
endPointHtml = 'https://'+ www +'.ngrok.io/html?id='
htmlPath = '../maps/'
HTMLROUTE = '/html'

TYPES_SIMPLEGRAPH = ['pie', 'histogram', 'line graph', 'scatter plot']
TYPES_COMPLEXGRAPH = ['scatter plot (X vs Y)', 'line graph (X vs Y)', 'scatter plot (series)', 'line graph (series)']


@app.route(FILEROUTE, methods=['GET'])
def getFiles():
    '''
    Send the requested file.
    '''
    id = request.args.get('id')
    filename = filesPath + id + '.txt'
    return send_file(filename, as_attachment=True)


@app.route(HTMLROUTE, methods=['GET'])
def gethtml():
    '''
    Send the requested file.
    '''
    id = request.args.get('id')
    filename = htmlPath + id + 'FoliumMap.html'
    return send_file(filename, as_attachment=True)


@app.route(IMAGESROUTE, methods=['GET'])
def getImage():
    id = request.args.get('id')
    filename = imagesPath + id + '.png'
    '''
    if os.path.isfile(filename):
        return send_file(filename, mimetype='image/gif')
    else:
        return send_file(IMAGE_NOT_FOUND, mimetype='image/gif')
    '''
    return send_file(filename, mimetype='image/gif')


@app.route(MAPSROUTE, methods=['GET'])
def getMapImage():
    id = request.args.get('id')
    filename = mapsPath + id + '.png'
    return send_file(filename, mimetype='image/gif')


# ruta por defecto
@app.route('/', methods=['POST'])
def index():
    # respuesta por defecto
    res = None
    # build a request object
    req = rqst.Request(request.get_json(force=True))

    #app.logger.info(hola)
    # if intent is for querys without WHERE
    '''
    if 'nowhere' in req.intent:
        res = nowhereIntent(req)
    # if intent is for querys with WHERE
    elif 'where' in req.intent:
        res = whereIntent(req)
    elif req.intent == SIMPLEGRAPH_INTENT:
        res = simpleGrapIntent()
    elif req.intent == TYPESIMPLEGRAPH_INTENT:
        res = typeSimpleGraphIntent(req)
    elif req.intent == TYPECOMPLEXGRAPH_INTENT:
        res = typeComplexGraphIntent(req)
    elif req.intent == COMPLEXGRAPH_INTENT:
        res = complexGraphIntent(req)
    elif req.intent == GETIMAGE_INTENT:
        res = getImageIntent(req)
    elif req.intent == MAP_INTENT:
        res = getMapIntent(req)
    elif req.intent == GETMAPFROMID_INTENT:
        res = getMapImageIntent(req)
    elif req.intent == HELP_INTENT:
        res = getCommandsIntent(req)
    '''
    if req.intent == 'intent1_where':
        res = intent1()
    elif req.intent == 'intent2_nowhere':
        res = intent2()
    elif req.intent == 'intent3_where':
        res = intent3()
    else:
        r = response.Response(None, 'Can you repeat it?')
        res = r.simple
    return res

def intent1():
    query = "select tititu from library where prcolp='PRO';"
    r = response.Response(None, 'The result has more lines than allowed. Please download the result here:\n' + 'https://' + www + '.ngrok.io/files?id=20200824185330Sndr18')
    res = r.simple
    return res

def intent2():
    query = 'select tititu from library;'
    r = response.Response(None, "The result is:\nALU,\nDIG,\nENT,\nINS,\nINV,\nLEC,\nLECI,\nPRO,\nROB,\nTEL,\n")
    res = r.simple
    return res

def intent3():
    query = "select tititu from library where prfpre='01/07/20' and prlesu='BCDIG';"
    r = response.Response(None, "The result is: \nLas aventuras del joven Einstein ,\nLa vuelta al mundo en 80 días ,\nQuerido zoo ,\nI'm not a supermouse ,\nMarada : la mujer lobo ,\nPenny Dreadful causes a kerfuffle ,\nRecuerdos del ayer ,\nQue Dios nos perdone ,\nDogman ,\n")
    res = r.simple
    return res

def getCommandsIntent(req):
    command = req.command
    res = None
    if command == 'help':
        res = {
            "fulfillmentMessages": [{
                "payload": {
                    "telegram": {
                        "text": 'Esta es la ayuda',
                    }
                },
                "platform": "TELEGRAM"
            }]
        }
    return jsonify(res)


def getMapIntent(req):
    id = getId()
    iduser = id + req.user
    getMap({req.fieldMap: req.valueMap}, req.tablename, req.databasename, iduser, req.long, req.lat, req.extrainfo)
    r = response.Response(id, None)
    return r.map


def getImageIntent(req):
    id = req.idFromReq + req.user

    res = getResponseWithImage('Here is your graph for one field.', endPointImages, id, imagesPath)
    return res


def getMapImageIntent(req):
    print(req.idFromReq)
    print(req.user)
    id = req.idFromReq + req.user
    text = 'Here is the interactive map:\n' + endPointHtml + id + '\n Here is your static map:\n'
    res = getResponseWithImage(text, endPointMaps, id, mapsPath)
    return res


def simpleGrapIntent():
    # ask to user for graph type
    r = response.Response(None, None)
    res = r.simpleGraph
    return res


def typeSimpleGraphIntent(req):
    tablename = req.tableName
    databasename = req.databaseName
    field = req.simpleGrapField
    type = req.typeSimpleGraph
    id = getId() + req.user
    print(type)
    if type == TYPES_SIMPLEGRAPH[0]:
        getPieChart(field, tablename, databasename, id)
    elif type == TYPES_SIMPLEGRAPH[1]:
        getHistogram(field, tablename, databasename, id)
    elif type in (TYPES_SIMPLEGRAPH[2], TYPES_SIMPLEGRAPH[3]):
        getSeriesGraph(field, tablename, databasename, type, id)
    r = response.Response(id, None)
    res = r.image
    return res


def getHistogram(field, tablename, databasename, id):
    h = histogram.Histogram(field, tablename, databasename, id)
    thread1 = threading.Thread(target=h.getHistogram)
    thread1.start()


def getMap(field, tablename, databasename, id, longitud, latitud, extrainfo):
    m = map.Map(field, tablename, databasename, id, longitud, latitud, extrainfo)
    thread1 = threading.Thread(target=m.getMap)
    thread1.start()


def getPieChart(field, tablename, databasename, id):
    p = pie.Pie(field, tablename, databasename, id)
    thread1 = threading.Thread(target=p.getPie)
    thread1.start()


def getSeriesGraph(field, tablename, databasename, type, id):
    s = serie.Serie(field, tablename, databasename, type, id)
    thread1 = threading.Thread(target=s.getSerie)
    thread1.start()


def complexGraphIntent(req):
    # ask to user for graph type
    r = response.Response(None, None)
    res = r.complexGraph
    return res


def typeComplexGraphIntent(req):
    tablename = req.tableName
    databasename = req.databaseName
    fields = req.graphFields
    #idH = getGraph(field1, field2, tablename, databasename)
    #res = getResponseWithImage('Here your graph.', endPointImages, idH)
    type = req.typeComplexGraph
    id = getId()
    iduser = id + req.user
    getComplexGraph(fields, tablename, databasename, type, iduser)
    r = response.Response(id, None)
    res = r.image
    return res


def getComplexGraph(fields, tablename, databasename, type, id):
    g = graph.Graph(fields, tablename, databasename, type, id)
    thread1 = threading.Thread(target=g.getGraph)
    thread1.start()


def getId():
    return time.strftime("%Y%m%d%H%M%S")


def executeQuery(query, databasename):
    result = DBERRORS[2]
    con = None
    try:
        # conectar con la bd
        con = db.DB("localhost", "root", "", databasename, 3306)
        result = con.select(query)

    except Exception as e:
        print(e)
        traceback.print_exc()

    finally:
        # si la conexion se ha creado --> cerrarla
        if (con):
            con.close()
        return result


def whereIntent(req):
    # respuesta por defecto
    response = 'Server error, please rephrase your request.'
    tablename = req.tableName
    db = req.databaseName

    # fetch action from json
    # get parameters from request
    parameters = req.parameters
    # get dict with values and columns names for query where
    where = getWhereValues(parameters, tablename)
    # get list with columns names for query select
    select = getSelectValues(parameters, tablename)

    # get all query
    query = getQuery(select, where, tablename)

    # exe query
    result = executeQuery(query, db)

    response = getResponse(result, query)
    # return a fulfillment response
    return response


def nowhereIntent(req):
    # respuesta por defecto
    response = 'Server error, please rephrase your request.'
    tablename = req.tablename
    db = req.databasename

    # get list with columns names for query select
    select = req.columns_select
    print(select)

    query = None
    if select:
        # get all query
        query = getQuery(select, None, tablename)
    # exe query
    result = executeQuery(query, db)

    #app.logger.info(str(result))

    # return a fulfillment response
    response = getResponse(result, query)
    return response


def getResponse(result, query):
    response = None
    if type(result) is list and len(result) > 15:
        idFile = saveResultToFile(result)
        url = getURLFromIdFile(idFile)
        response = 'The result has more lines than allowed. Please download the result here: \n' + url
    else:
        response = 'RESULT: \n'
        if result in DBERRORS:
            response = response + result + '\n'
        else:
            for item in result:
                response = response + '- ' + item + '\n'
        response = response + 'QUERY: \n' + query
    # return a fulfillment response
    return jsonify({'fulfillmentText': response})


def saveResultToFile(result):
    '''
    Save results from db to a txt file.
    '''
    fileId = time.strftime("%Y%m%d%H%M%S")
    pathFile = filesPath + fileId + '.txt'
    file = open(pathFile, 'w')
    for item in result:
        file.write(str(item) + '\n')
    file.close()
    return fileId


def getURLFromIdFile(idFile):
    '''
    Return the url of a file with its ID.
    '''
    return endPointFiles + idFile


# return a string with SQL query
def getQuery(select, where, tableName):
    # first part of query
    query = 'SELECT '

    for item in select:
        query = query + item + ', '

    # remove the last comma and space
    query = query[:-2]
    query = query + ' FROM ' + tableName

    # if there ashow me on map the pharmacy of Mercedes Valdes Galerare where clause
    if where:
        query = query + ' WHERE '

        for key in where:
            query = query + 'SOUNDEX(LOWER(' + key + ')) = ' + "SOUNDEX('" + str(where[key]).lower() + "') and "

        query = query[:-5]
    return query + ';'


def getWhereValues(parameters, tableName):
    '''
    Returns a dict with values and columns names for querys.
    '''
    where = {}
    index = {}
    for key in parameters:
        if key not in ['columns_select', 'columns_where', 'tablename', 'databasename'] and key not in defaultEntities:
            if parameters[key] != '' and parameters[key] != []:
                keyWhere = str(key)[len(str(key).split('_')[0]) + 1:]
                where[keyWhere] = str(parameters[key]).strip()

    if 'columns_where' in parameters.keys():
        if len(parameters['columns_where']) == getLenDefaultEntities(parameters):
            for item in parameters['columns_where']:
                nameEntity = item.split('_')
                if index.get(nameEntity[0]) or index.get(nameEntity[0]) == 0:
                    index[nameEntity[0]] += 1
                else:
                    index[nameEntity[0]] = 0
                app.logger.info(index[nameEntity[0]])
                app.logger.info(index.get(nameEntity[0]))
                #where[nameEntity[1] + '_' + nameEntity[2]] = parameters[nameEntity[0]][index[nameEntity[0]]]
                where[nameEntity[2]] = str(parameters[nameEntity[0]][index[nameEntity[0]]]).strip()

    return where


def getLenDefaultEntities(parameters):
    '''
    Returns the length of the default entity values
    '''
    leng = 0
    for key in parameters:
        if key in defaultEntities:
            leng = leng + len(parameters[key])
    return leng


def getSelectValues(parameters, tableName):
    '''
    Returns a list with columns names for query select.
    '''

    select = [str(item)[len(str(item).split('_')[0]) + 1:] for item in parameters['columns_select']]
    return select


def getResponseWithImage(text, endPointImages, idImage, path):
    filename = path + idImage + '.png'
    if os.path.isfile(filename):
        res = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "telegram": {
                            "text": text
                        }
                    },
                    "platform": "TELEGRAM"
                },
                {
                    "image": {
                        "imageUri": endPointImages + idImage
                    },
                    "platform": "TELEGRAM"
                }
            ]
        }
    else:
        res = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "telegram": {
                            "text": 'Wait a while until the server completes the graph.'
                        }
                    },
                    "platform": "TELEGRAM"
                }
            ]
        }

    return res


if __name__ == '__main__':
    try:
        # run
        app.run(debug=True)

    except Exception as e:
        print(e)
