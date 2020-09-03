import json
import copy
import csv
import io
import itertools
'''
{
  "apiVersion": "API_VERSION_V2",
  "parent": "projects/sqlBot-1562750179610",
  "displayName": "sqlBot-Plaques",
  "defaultLanguageCode": "en",
  "timeZone": "Europe/Paris"
}

 Email address
starting-account-ot5v5awrmv31@sqlbot-1562750179610.iam.gserviceaccount.com
Key IDs
36cc9590dc635e9970c5c5373b067b0161f0dd23

export GOOGLE_APPLICATION_CREDENTIALS="/home/miso/REPO/chatbots/Sandra/sqlBot/jsonAgent/sqlBot-36cc9590dc63.json"

'''


allowedChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','_','1','2','3','4','5','6','7','8','9','0']

# table name
tableName = "plaques"

# global id for phrases
idCount = 0

# global id for intents
idIntents = 0

# number of rows to get from csv
sample = 6

# [nameIntent].json content
intent = {
    "id": "",
    "name": "",
    "auto": True,
    "contexts": [],
    "responses": [
        {
            "resetContexts": False,
            "affectedContexts": [],
            "parameters": [],
            "messages": [
            {
                "type": 0,
                "lang": "en",
                "speech": []
            }
            ],
            "defaultResponsePlatforms": {},
            "speech": []
        }
    ],
    "priority": 500000,
    "webhookUsed": False,
    "webhookForSlotFilling": False,
    "fallbackIntent": False,
    "events": []
}

# [nameIntent]_usersays_en.json content
# to represent one training phrase
sentence = {
    "id": 0,
    "data": [],
    "istemplate": False,
    "count": 0
}

# to represent plain text in training phrases
simpleWord = {
    "text": "",
    "userDefined": False
}

# to represent entity in training phrases
entityWord = {
    "text": "",
    "alias": "",
    "meta": "",
    "userDefined": False
}

# [nameEntity].json content
entity = {
    "id": 0,
    "name": "",
    "isOverridable": True,
    "isEnum": False,
    "isRegexp": False,
    "automatedExpansion": False,
    "allowFuzzyExtraction": False
}
# [nameEntity]_entries_en.json content
entity_entry = {
    "value": "",
    "synonyms": []
 }

# structure for phrases
phraseStructure = {
    "order" : 0,
    "type" : "",
    "value" : []
}

# data to work
data = {
    "column-name" : "",
    "entity-name" : "",
    "sample-values" : ""
}

rows = []

def createTrainingPhrases(file, ithasValues):
    '''
    Create training phrases for intents according to a model in especified file.
    Depending on the "ithasValues" value (True or False), it will be created
    training phrases with or without values.
    '''
    # read from file
    # model phrases
    phrases = readTrainPhrases(file)
    # choose model phrases from file with or without "where"
    phrases = phrasesFilter(ithasValues, phrases)
    # create list with training phrases
    phrasesJson = [createPhrasesJson(p) for p in phrases]
    # join in a unique list
    phrasesJson = [j for i in phrasesJson for j in i]
    #phrasesJson = list(itertools.chain(*phrasesJson))
    #print(phrasesJson)
    return phrasesJson

def createPhrasesJson(phrase):
    '''
    Create training phrases to insert in json files.
    '''
    # create combination of columns and values
    listToCombine = createListToCombine(phrase)
    combinedValues = combineValuesAndColumns(listToCombine)
    print(combinedValues)
    phraseStructure = createPhraseStructure(phrase)
    return createMultiplePhrasesWithStructure(phraseStructure)

def createListToCombine(phrase):
    '''
    Creates a combinated list with values and names columns from example phrase.
    '''
    foundFirstPercentage = False
    foundFirstAmpersand = False
    isSimpleWord = False
    combinatedList = []
    data = ''

    for i, char in enumerate(phrase):
        if char == '%':
            # if first % had been found and last % is found --> save column entity
            if foundFirstPercentage:
                # save phrase part into array
                if i == 0:
                    combinatedList = [data.split(',')]
                else:
                    combinatedList.append(data.split(','))
                # reset value to false
                foundFirstPercentage = False
            else:
                # first percentaje is founf and set value to True
                foundFirstPercentage = True
            data = ''
        elif char == '&':
            # if first & had been found and last & is found --> save column entity
            if foundFirstAmpersand:
                if i == 0:
                    combinatedList = [data.split(',')]
                else:
                    combinatedList.append(data.split(','))
                # reset value to false
                foundFirstAmpersand = False
            else:
                # if is first percentaje set value to True
                foundFirstAmpersand = True
            data = ''
        else:
            data = data + char
            if not foundFirstAmpersand and not foundFirstPercentage:
                isSimpleWord = True
    return combinatedList


def phrasesFilter(hasValue, phrases):
    if hasValue:
        phrasesWithFilter = [p for p in phrases if hasValues(p)]
    else:
        phrasesWithFilter = [p for p in phrases if not hasValues(p)]

    return phrasesWithFilter

def hasValues(phrase):
    hasValues = False
    for letter in phrase:
        if letter == '&':
            hasValues = True
    return hasValues


def isColumnNameEntity(word):
    alias = word.get('alias')
    if alias and 'columns_select' in alias:
        return True
    else:
        return False

def isValueEntity(word):
    alias = word.get('alias')
    if alias  != None and alias == "":
        return True
    else:
        return False

def createMultiplePhrasesWithStructure(structure):
    '''
    Genere all combinations of values from structure to make training phrases.
    Make all training phrases with the combination above.
    '''
    combinedValues = combineValuesAndColumns(structure)
    #phraseList = createPhrases(combinedValues)
    #print(combinedValues)
    returnPhrases = []
    for i, t in enumerate(combinedValues):
        metadata = copy.deepcopy(sentence)
        metadata['id'] = i
        metadata['data'] = createPhrase(t, structure)
        if i == 0:
            returnPhrases = [metadata]
        else:
            returnPhrases.append(metadata)
    #return [createPhrase(tuple, structure) for tuple in combinedValues]
    return returnPhrases

def createPhrase(tupleValues, structure):
    '''
    Create one training phrase with value tuple and structure.
    '''
    print(structure)
    print(tupleValues)
    index = 0
    # we consider that the orden of elements in structure is the correct for training phrases.
    for word in structure:
        if word['type'] == 'value':
            phrasePart = copy.deepcopy(entityWord)
            phrasePart['text'] = tupleValues[index]
            index += 1
        elif word['type'] == 'column':
            phrasePart = copy.deepcopy(entityWord)
            phrasePart['text'] = tupleValues[index][1]
            if 'sys.' in tupleValues[index][0]:
                word['alias'] = tupleValues[index][0][4:]
            else:
                word['alias'] = tupleValues[index][0]
            word['meta'] = '@' + tupleValues[index][0]
            index += 1
        elif word['type'] == 'plain-text':
            phrasePart = copy.deepcopy(simpleWord)
            phrasePart['text'] = word['value']
    #for word in phrase:
    #    if word
    return phrase


def createValuesWithNameEntity(values):
    #del values[0:4]
    listFinal = []
    for i, row in enumerate(values):
        nameEntity = row[0]
        del row[0:2]
        list = [[nameEntity, value] for value in row]
        if i == 0:
            listFinal = [list]
        else:
            listFinal.append(list)
    #print(values)
    return listFinal

def listToString(list):
    '''
    With a given list return another with all elements cast to string.
    Method used to remove unicode annotation.
    '''
    return [str(item) for item in list]

def combineValuesAndColumns(listToCombine):
    '''
    Return a list with all posible values and columns names combinations given a list.
    '''
    return [comb for comb in itertools.product(*listToCombine)]

def isComment(line):
    if line[0] == '#':
        return True
    else:
        return False

def readTrainPhrases(file):
    f = open(file, "r")
    lines = []
    with open(file) as f:
        content = f.readlines()
        # scape comments
        lines = [line for line in content if not isComment(line)]
        #lines = [line.strip() for line in content]
        #lines = [str(line) for line in f]
    return lines

def createIntents(PhrasesPath, pathToWrite, table):
    '''
    Create all intents files for Dialogflow agent.
    '''
    # global id to not repeat id
    global idIntents
    fileName =  pathToWrite + '/intents/' + table['table_name']

    # create intents for query with where
    phrasesWhere = createTrainingPhrases(PhrasesPath, True)
    # if there are phrases with "where":
    if phrasesWhere:
        writeToFile(phrasesWhere, fileName + '_where_usersays_en.json')
        createIntentFile(pathToWrite, table['table_name'] + '_where', idIntents)
        idIntents = idIntents + 1

    # create intents for query without where
    phrasesNoWhere = createTrainingPhrases(PhrasesPath, False)
    # if there are phrases without "where":
    if phrasesNoWhere:
        writeToFile(phrasesNoWhere, fileName + '_nowhere_usersays_en.json')
        createIntentFile(pathToWrite, table['table_name'] + '_nowhere', idIntents)
        idIntents = idIntents + 1

def createIntentFile(pathToWrite, fileName, id):
    file = copy.deepcopy(intent)
    file['id'] = id
    file['name'] = fileName
    writeToFile(file, pathToWrite + '/intents/' + fileName + '.json')


# create all entities files: [columnName].json and [columnsName]_entries_en.json
# each entity has two json files
def createAllEntitiesFiles(tablename, list):
    # control id for entities
    id = 0
    # create entities for each field/column in data
    for i, item in enumerate(list):
        if item['entity_type'] == 'None':
            createEntityFile(item, tableName, i, True)
            createEntityEntriesFile(tablename, item)
            id = i
    # create entity [columns_select_tablename]
    id = id + 1
    createEntitySelectFile(tablename, id, False)
    createEntityEntriesSelectFile(tablename, list)
    # create entity [columns_where_tablename]
    id = id + 1
    createEntityWhereFile(tablename, id, False)
    createEntityEntriesWhereFile(tablename, list)


# create entity file: [tablename_columnName].json
def createEntityFile(item, tableName, id, automatedExpansion):
    filename = "./v3/entities/" + tableName + "_" + item['field_name'] + ".json"
    e = copy.deepcopy(entity)
    e['id'] = id
    e['name'] = tableName + "_" + item['field_name']
    e['automatedExpansion'] = automatedExpansion
    writeToFile(e, filename)

# create entity file: [tablename_columnName]_entries_en.json
def createEntityEntriesFile(tablename, item):
    filename = "./v3/entities/" + tableName + "_" + item['field_name'] + "_entries_en.json"
    items = []
    for i, s in enumerate(rows[item['order']]):
        if i >= 3:
            e = copy.deepcopy(entity_entry)
            e['value'] = rows[item['order']][i]
            e['synonyms'] = [s]
        if i == 3:
            items = [e]
        elif i > 3:
            items.append(e)
    writeToFile(items, filename)

# create entity file: columns_select.json
def createEntitySelectFile(tablename, id, automatedExpansion):
    filename = "./v3/entities/columns_select_" + tablename + ".json"
    e = copy.deepcopy(entity)
    e['id'] = id
    e['name'] = "columns_select_" + tablename
    e['automatedExpansion'] = automatedExpansion
    writeToFile(e, filename)

# create entity file: columns_select_entries_en.json
def createEntityEntriesSelectFile(tablename, list):
    filename = "./v3/entities/columns_select_" + tablename + "_entries_en.json"
    synonyms = []
    items = []
    for i, item in enumerate(list):
        e = copy.deepcopy(entity_entry)
        e['value'] = item['field_name']
        for j, s in enumerate(item['synonyms']):
            if j == 0:
                synonyms = [s]
            else:
                synonyms.append(s)
        e['synonyms'] = synonyms
        if i == 0:
            items = [e]
        else:
            items.append(e)
    writeToFile(items, filename)

# create entity file: columns_where.json
def createEntityWhereFile(tablename, id, automatedExpansion):
    filename = "./v3/entities/columns_where_" + tablename + ".json"
    e = copy.deepcopy(entity)
    e['id'] = id
    e['name'] = "columns_where_" + tablename
    e['automatedExpansion'] = automatedExpansion
    writeToFile(e, filename)

# create entity file: columns_where_entries_en.json
def createEntityEntriesWhereFile(tablename, list):
    filename = "./v3/entities/columns_where_" + tablename + "_entries_en.json"
    synonyms = []
    items = []
    for i, item in enumerate(list):
        e = copy.deepcopy(entity_entry)
        e['value'] = item['field_name']
        for j, s in enumerate(item['synonyms']):
            if j == 0:
                synonyms = [s]
            else:
                synonyms.append(s)
        e['synonyms'] = synonyms
        if i == 0:
            items = [e]
        else:
            items.append(e)
    writeToFile(items, filename)


def getSampleAndStructuredData(file, thereIsHead, tableStructure):
    '''
    Reads a sample of rows from csv and creates structured list of columns with values and information for work.
    '''
    # get a sample of rows
    rows = readCsvAndGetRows(file, thereIsHead)
    # get structured data to work
    structuredData = getStructuredData(rows, tableStructure)
    return structuredData

def getStructuredData(rows, tableStructure):
    '''
    Creates a list of columns with values and information for work.
    '''
    # traspose data --> rows into columns
    columns = []
    for i in range(0, len(rows[1])):
        col = [rows[j][i] for j in range(0, sample-1)]
        if i == 0:
            columns = [col]
        else:
            columns.append(col)
    return columns

def readCsvAndGetRows(file, thereIsHead):
    '''
    Read csv and return a sample values for training phrases.
    '''
    with open(file) as File:
        reader = csv.reader(File)
        # position to stop reading
        stop = sample
        # if there is a head with columns names in csv --> get one more csv line
        if thereIsHead:
            stop = sample + 1
        rows = []
        # iterate over all lines in csv
        for i, row in enumerate(reader):
            if i <= stop:
                if i == 0:
                    rows = [row]
                else:
                    rows.append(row)
            else:
                break
    if thereIsHead:
        rows = rows[1:]
    return rows

def readCsvAndSaveSampleInMemory(file, fields, thereIsHead):
    # TODO comprobar si hay cabecera o no
    rows = []
    # read csv
    # open csv
    # extract sample data
    with open(file) as File:
        reader = csv.reader(File)
        for i, row in enumerate(reader):
            if i < sample and i != 0:
                if i == 1:
                    rows = [row]
                else:
                    rows.append(row)
            elif i == 0:
                columnsNames = row
            else:
                break

    # format extracted data to save in memory
    columns = []
    for i in range(0, len(rows[1])):
        col = []
        for j in range(0, sample-1):
            if j == 0:
                col = [rows[j][i]]
            else:
                col.append(rows[j][i])
        if i == 0:
            columns = [col]
        else:
            columns.append(col)
    #print(columns)

    # insert in extracted data the column name and entity type.
    # this info (column name, entity type...) is taken from db schema
    for i in range(0, len(rows[1])):
        # name entities
        field = findFieldWithOrder(i, fields)
        columns[i].insert(0, clearData(field['field_name'], ''))

        # type entity
        # default type is field_name + tableName
        # default type in model --> field['entity_type'] == 'None'
        if field['entity_type'] == 'None':
            type = tableName + "_" + field['field_name']
        # if not default type
        # in model --> field['entity_type'] != 'None'
        else:
            type = field['entity_type']
        columns[i].insert(0, type)

        # column name
        columns[i].insert(0, clearData(field['field_name'], ''))

    return columns


def findFieldWithOrder(order, list):
    '''
    Find a column in given list with an order
    '''
    for f in list:
        if f['order'] == order:
            return f
    return None


def clearData(string, charToPut):
    '''
    Clear data from invalid character.
    Invalid characters will be changed by specified character.
    '''
    string = list(string)
    for i in range(0, len(string)):
        if not string[i] in allowedChar:
            string[i] = charToPut
    string = ''.join(string)
    return string


# write json to a file
def writeToFile(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

'''
def encodeUTF8(a):
  for list in a:
    return [x.encode('utf-8') for x in list]
'''
#def formatNumbersAndDates():

def readModelFromFile(file):
    model = None
    with open(file, 'r') as f:
        model = json.load(f)
    return model

# main
def main():

    csvPath = "../data/Placas_memoriademadrid.csv"
    trainingPhrasesPath = "./phrases"
    intentsPath = "./v3"
    headers = True

    # read model from file json
    # this model contains db schema
    model = readModelFromFile("./schema_v2.json")

    # for each table --> create entities and intents
    for table in model['tables']:
        # read data from CSV and save a sample
        sampleData = getSampleAndStructuredData(csvPath, headers, table)
        createIntents(trainingPhrasesPath, intentsPath, table)

        #createAllEntitiesFiles(table['table_name'], table['fields'])



    # create phrases with type 1
    #sentences = []
    #sentences = createType1Phrases()

    # create phrases with type 1
    #createType2Phrases(sentences)
    #print(sentences)
    # write data to a file
    #writeToFile(sentences, './v3/intents/Plaques_usersays_en.json')


    #clearData("hola soy .,", '_')


if __name__ == '__main__':
   main()
