from flask import Flask
from flask import request
from flask import send_file
from flask import jsonify
from model import DataBase as database
from model import UserData as userdata
from model import Field as field
from model import Table as table
from model import Properties as properties
from model import InfoMap as infoMap
from responses import Response as response
from request import Request as rqst
from utils import utils
from plantuml import Plantuml as puml
from entities import createAllEntities as entity
from intents import createAllIntents as intent
import pprint
from db import dbutils
import time


class NoField(Exception):
    pass


class NoType(Exception):
    pass


# to persits user data
persistData = []

app = Flask(__name__)

endPointImages = 'https://d2b4041f8d50.ngrok.io/images?id='
imagesPath = '../images/'

endPointChatbot = 'https://d2b4041f8d50.ngrok.io/chatbot?id='
chatbotPath = '../agents/'

trainingPhrasesPath = "../inputs/phrases"

sample = 10


@app.route('/images', methods=['GET'])
def getImage():
    id = request.args.get('id')
    filename = imagesPath + id + '.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/chatbot', methods=['GET'])
def getCdatehatbot():
    id = request.args.get('id')
    filename = chatbotPath + id + '.zip'
    return send_file(filename)

@app.route('/csv', methods=['GET'])
def getCSV():
    return send_file('../csv/farmacias.csv')

@app.route('/', methods=['POST'])
def requestAnalizer():
    global persistData
    # respuesta por defecto
    res = None
    # info from csv
    # build a request object
    app.logger.info('-------------------')
    #pp = pprint.PrettyPrinter(indent=2)
    #pp.pprint(request.get_json(force=True))
    req = rqst.Request(request.get_json(force=True))


    print(req.user)

    # si el intent es appointments comprobar los detalles de la cita
    if req.intent == 'DB name':
        res = dbName_intent(req)

    elif req.intent == 'Table name':
        res = tablename_intent(req)

    elif req.intent == 'Csv Path':
        res = csv_intent(req)

    elif req.intent == 'Field synonyms':
        res = synonyms_intent(req)
    # change db type
    elif req.intent == 'Change DB_Type - yes':
        res = showButtonsToChangeType(req)

    elif req.intent == 'Change DB_Type - no':
        res = changeDFType_intent(req)

    elif req.intent == 'Change DB_Type - field':
        res = showButtonsToChooseType(req, 'DB_Type')

    elif req.intent == 'Change DB_Type - type':
        res = changeDBType(req)
    # change df type
    elif req.intent == 'Change Dialogflow_Type - yes':
        res = showButtonsToChangeType(req)

    elif req.intent == 'Change Dialogflow_Type - no':
        res = askForMaps_intent(req)

    elif req.intent == 'Change Dialogflow_Type - field':
        res = showButtonsToChooseType(req, 'DF_Type')

    elif req.intent == 'Change Dialogflow_Type - type':
        res = changeDFType(req)

    elif req.intent == 'Yes info - maps':
        res = ask_coor(req, 'x')

    elif req.intent == 'Get coordinates':
        res = getCoor_intent(req)

    elif req.intent == 'Get valueMap':
        res = getValueMap_intent(req)

    elif req.intent in ('No info - maps', 'Get extraInfo - no'):
        res = finishTalk(req)

    elif req.intent == 'Get extraInfo':
        res = get_extraInfo(req)

    app.logger.info('EL INTENT ES:     ' + str(req.intent))
    print('ya')
    #pp = pprint.PrettyPrinter(indent=2)
    #pp.pprint(persistData)
    #print(res)
    return jsonify(res)


def dbName_intent(req):
    global persistData
    # create model
    db = database.DataBase(req.dbname, None)
    data = userdata.UserData(req.user, db, None)
    # save data
    save_data(data)
    # create response
    text = "Saved!\nNow tell me the name of the table you want add to the database."
    r = response.Response(text, None, [], [], None)
    res = r.response
    return res


def tablename_intent(req):
    # get model by username
    data = getUserData(req.user)
    # create table and add to user data
    data.db.table = table.Table(req.tablename, '', None)
    # generate response
    text = "Ok, saved!\nNow I need the csv url of '" + req.tablename + "' table."
    r = response.Response(text, None, [], [], None)
    res = r.response
    return res


def csv_intent(req):
    # get model by username
    data = getUserData(req.user)
    # add csv to table
    data.db.table.csv_url = req.csv
    # read csv
    df = utils.getDF(data.db.table)
    #utils.saveToCSV(df, data.db.table.csv_local)
    # create list of fields
    data.db.table.fields = [createField(df, i) for i in range(len(df.columns))]
    res = askForSynonyms(data)
    '''
    print('tablename: ' + data.db.table.name)
    print('csv: ' + data.db.table.csv_url)
    for field in data.db.table.fields:
        print('fieldname: ' + field.name)
        print('entity_meta: ' + field.entity_meta)
        print('db_meta: ' + field.db_meta)
    '''
    return res


def createField(df, i):
    f = field.Field(utils.clearData(df.columns[i], ''), [], i, [], '', '')
    f.values = df[df.columns[i]].sample(n=sample, random_state=1).tolist()
    col = df.iloc[:, i]
    if col.dtype == 'float64':
        f.db_meta = 'decimal(10,8)'
        f.entity_meta = 'sys.number'
    elif col.dtype == 'int64':
        f.db_meta = 'integer'
        f.entity_meta = 'sys.number'
    elif col.dtype in ('object', 'string_', 'unicode_'):
        col = col.astype('unicode')
        maxlen = max(col.apply(len))
        f.db_meta = 'varchar(' + str(maxlen) + ')'
        f.entity_meta = 'None'
    elif col.dtype == 'datetime64':
        f.db_meta = 'date'
        f.entity_meta = 'sys.date'
    return f


def askForSynonyms(model):
    text = None
    context = []
    image = None
    buttons = []
    field = getFirstFieldWithoutSynonyms(model.db.table)
    if field is None:
        text = "Done. This table is already complete.\nThe model created is as follow.\nDo you want to make some changes in DB_Type? (yes/no).\n\nNOTE: DB_Type is the type of fields in database."
        context = [{
            "name": "projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/csvpath-followup",
            "lifespanCount": 0
        }]
        buttons = [['Yes', 'No']]
        p = puml.Plantuml(model)
        idPlantumlImage = p.getPlantumlImage()
        image = endPointImages + idPlantumlImage
    else:
        text = u'Ok, now I need you tell me the synonyms for "' + str(field.name) + u'" field \nHere a sample of data stored in "' + str(field.name) + u'" field: ' + str(field.values[0]) + ', ' + str(field.values[1]) + u', ' + str(field.values[2]) + u'.\n\nNOTE: separate synonyms with commas.'
        context = [{
            "name": "projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/csvpath-followup",
            "lifespanCount": 2
        }]
    r = response.Response(text, image, buttons, [], context)
    res = r.response
    return res


def getFirstFieldWithoutSynonyms(tble):
    field = None
    for f in tble.fields:
        if f.synonyms == []:
            field = f
            break
    return field


def synonyms_intent(req):
    res = None
    # get model by username
    data = getUserData(req.user)
    field = getFirstFieldWithoutSynonyms(data.db.table)
    if field is not None:
        field.synonyms = req.synonyms
        res = askForSynonyms(data)
    else:
        text = "Some error..."
        context = [{
            "name": "projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/csvpath-followup",
            "lifespanCount": 0
        }]
        r = response.Response(text, None, [], [], context)
        res = r.response
    return res


def changeDFType_intent(req):
    text = "Done. This table is already complete.\nThe model created is as follow.\nDo you want to make some changes in DF_Type? (yes/no).\n\nNOTE: DF_Type is the type of entity in Dialogflow for a field."
    context = [{
        "name": "projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/csvpath-followup",
        "lifespanCount": 0
    }]
    buttons = [['Yes', 'No']]
    p = puml.Plantuml(getUserData(req.user))
    idPlantumlImage = p.getPlantumlImage()
    image = endPointImages + idPlantumlImage
    r = response.Response(text, image, buttons, [], context)
    print(image)
    print(r)
    res = r.response
    return res


def showButtonsToChangeType(req):
    text = 'Choose the field you want to change.'
    # get data by username
    data = getUserData(req.user)
    inline = []
    for f in data.db.table.fields:
        inline.append([{'text': f.name, 'callback_data': data.db.table.name + '/' + f.name}])
    r = response.Response(text, None, [], inline, None)
    res = r.response
    return res


def changeDBType(req):
    buttons = [["Yes", "No"]]
    text = "Don't find the field you entered. Dou you want to make more changes in df_type?"
    context = [
        {
            "name": 'projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/Fieldsynonyms-followup',
            "lifespanCount": 2
        },
        {
            "name": 'projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/ChangeDB_Type-field-followup',
            "lifespanCount": 0
        },
        {
            "name": 'projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/ChangeDB_Type-followup',
            "lifespanCount": 0
        }
    ]
    type = req.dbType
    data = getUserData(req.user)
    for f in data.db.table.fields:
        if f.name == req.fieldname:
            if type == 'varchar':
                f.db_meta = 'varchar(20)'
            elif type == 'decimal':
                f.db_meta = 'decimal(10,8)'
            else:
                f.db_meta = type
            text = 'Changed.\nDou you want to make more changes in db_type?'
            break
    r = response.Response(text, None, buttons, [], context)
    res = r.response
    return res


def changeDFType(req):
    text = "Don't find the field you entered.\nDou you want to make more changes in df_type?"
    buttons = [["Yes", "No"]]
    context = [{
        "name": 'projects/initbot-svhgjk/agent/sessions/8c5eec04-72b3-63cc-3e36-238695a1aa35/contexts/ChangeDB_Type-no-followup',
        "lifespanCount": 2
    }]
    type = req.dfType
    data = getUserData(req.user)
    for f in data.db.table.fields:
        if f.name == req.fieldname:
            if type == 'custom':
                f.entity_meta = 'None'
            else:
                f.entity_meta = 'sys.' + type.lower()
            text = 'Changed.\nDou you want to make more changes in df_type?'
            break
    r = response.Response(text, None, buttons, [], context)
    res = r.response
    return res


def showButtonsToChooseType(req, type):
    text = 'Choose the new type.'
    buttons = []
    if type == 'DB_Type':
        buttons = [['date'], ['integer'], ['varchar'], ['decimal']]
    else:
        buttons = [['number'], ['date'], ['url'], ['phone-number'], ['custom']]
    r = response.Response(text, None, buttons, [], None)
    res = r.response
    return res


def askForMaps_intent(req):
    text = 'You can find the final model in the following image.\n\nNow I need some info in order to create maps.\nDo your csv have fields with coordinates X and Y (longitude and latitude)? (yes/no).'
    buttons = [["Yes", "No"]]
    data = getUserData(req.user)
    p = puml.Plantuml(data)
    idPlantumlImage = p.getPlantumlImage()
    image = endPointImages + idPlantumlImage
    r = response.Response(text, image, buttons, [], None)
    res = r.response

    return res


def ask_coor(req, coordinate):
    textX = "Perfect, let's start.\nSelect the field for coordinate X (longitude)."
    textY = "Saved.\nSelect the field for coordinate Y (latitude)."
    text = ''
    data = getUserData(req.user)
    inline = []
    for f in data.db.table.fields:
        inline.append([{'text': f.name, 'callback_data': 'coordinate ' + coordinate + ' is ' + f.name}])
    if coordinate == 'x':
        text = textX
    else:
        text = textY
    r = response.Response(text, None, [], inline, None)
    res = r.response
    return res


def getCoor_intent(req):
    data = getUserData(req.user)
    coordinate = req.coordinate
    field = req.fieldname
    res = None

    if not data.properties:
        info_map = infoMap.InfoMap('', '', '', [])
        p = properties.Properties(info_map, [])
        data.properties = p
    if coordinate == 'x':
        data.properties.info_map.coorX_field = field
        res = ask_coor(req, 'y')
    elif coordinate == 'y':
        data.properties.info_map.coorY_field = field
        res = ask_valueMap(data)

    return res

def ask_valueMap(data):
    text = 'Good! The coordinates are saved.\n\nNow I need you tell me the field to ask for maps. Choose the field with the following buttons.'
    inline = []
    for f in data.db.table.fields:
        inline.append([{'text': f.name, 'callback_data': 'valueMap is ' + f.name}])
    r = response.Response(text, None, [], inline, None)
    res = r.response
    return res

def ask_extraInfo():
    text = 'The field to ask for maps is saved. Do you want add extra data in maps?'
    buttons = [["Yes", "No"]]
    r = response.Response(text, None, buttons, [], None)
    res = r.response

    return res

def get_extraInfo(req):
    data = getUserData(req.user)
    print(req.extraInfo)
    data.properties.info_map.extra_info_fields = req.extraInfo
    return finishTalk(req)

def getValueMap_intent(req):
    data = getUserData(req.user)
    field = None
    for f in data.db.table.fields:
        if f.name == req.fieldname:
            field = f
    data.properties.info_map.filter_field = field
    print(field.name)
    return ask_extraInfo()


def finishTalk(req):
    data = getUserData(req.user)
    id = getChatbotId(req.user)
    url = endPointChatbot + id
    text = "Perfect!\n\nThe talk has finished, I have created a prebuilt chatbot with the information you give me.\n\nCheck the following url to download it.\n\n" + url
    r = response.Response(text, None, [], [], None)
    res = r.response

    # create db on server
    dbutils.createDB(data.db)

    utils.removeCSV(data.db.table.csv_local)
    utils.clearDirs()
    entity.createAllEntities(data.db)
    intent.createAllIntents(data)

    utils.createAgent(id)


    return res

def save_data(data):
    global persistData
    if persistData is not []:
        # check if the user already has saved data
        for item in persistData:
            #delete if it exists
            if item.username == data.username:
                persistData.remove(item)
        # save
        persistData.append(data)
    else:
        persistData.append(data)


def getUserData(user):
    global persistData
    data = None
    for item in persistData:
        if item.username == user:
            data = item
            break
    return data

def getChatbotId(user):
    id = time.strftime("%Y%m%d%H%M%S") + user
    return id

# main
def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
