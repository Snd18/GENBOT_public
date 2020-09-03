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

rows = []

# create training phrases with or without values
def createTrainingPhrases(file, hasValues):
    phrases = readTrainPhrases(file)
    phrases = phrasesFilter(hasValues, phrases)
    phrasesJson = [createPhrasesJson(p) for p in phrases]
    # join in a unique list
    phrasesJson = [j for i in phrasesJson for j in i]
    #phrasesJson = list(itertools.chain(*phrasesJson))
    #print(phrasesJson)
    return phrasesJson

def createPhrasesJson(phrase):
    phraseStructure = createPhraseStructure(phrase)
    return createMultiplePhrasesWithStructure(phraseStructure)

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


'''
# check if an item is a simple word or entity word
def isAsimpleWord(word):
    # if item contains 'alias' is not a simple word
    word = word.get('alias')
    if word != None:
        return False
    else:
        return True
'''

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

'''
def createMultiplePhrasesWithStructure(structure):
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

'''

def createPhrase(tupleValues, structure):
    phrase = copy.deepcopy(structure)
    index = 0
    for word in phrase:
        if isColumnNameEntity(word):
            word['text'] = tupleValues[index]
            index += 1
        elif isValueEntity(word):
            word['text'] = tupleValues[index][1]
            if 'sys.' in tupleValues[index][0]:
                word['alias'] = tupleValues[index][0][4:]
            else:
                word['alias'] = tupleValues[index][0]
            word['meta'] = '@' + tupleValues[index][0]
            index += 1
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
    return [str(item) for item in list]

def combineValuesAndColumns(structure):
    '''
    # create list with column names and values for combine
    columnNames = [str(list[0]) for list in rows]
    values = [listToString(list[1:]) for list in rows]
    #print(values)
    # create name entity - value pair
    values = createValuesWithNameEntity(values)
    # join in a unique list
    values = [j for i in values for j in i]
    '''
    listToCombine = [part['value'] for part in structure]
    print(listToCombine)
    '''
    for i, word in enumerate(structure):
        #if not isAsimpleWord(word):
        if isColumnNameEntity(word):
            if i == 0:
                listToCombine = [columnNames]
            else:
                listToCombine.append(columnNames)
        elif isValueEntity(word):
            if i == 0:
                listToCombine = [values]
            else:
                listToCombine.append(values)
    '''
    return [comb for comb in itertools.product(*listToCombine)]

def createPhraseStructure(phrase):
    foundFirstPercentage = False
    foundFirstAmpersand = False
    isSimpleWord = False
    structure = []
    data = ''

    for i, char in enumerate(phrase):
        phrasePart = copy.deepcopy(phraseStructure)
        if char == '%':
            # if first % had been found and last % is found --> save column entity
            if foundFirstPercentage:
                phrasePart['order'] = len(structure)
                phrasePart['type'] = 'column'
                phrasePart['value'] = [item.strip() for item in data.split(',')]
                # save phrase part into array
                if i == 0:
                    structure = [phrasePart]
                else:
                    structure.append(phrasePart)
                # reset value to false
                foundFirstPercentage = False
            else:
                # first percentaje is founf and set value to True
                foundFirstPercentage = True
                # save data if previous data is a simple word
                if data != '' and isSimpleWord:
                    isSimpleWord = False
                    phrasePart['order'] = len(structure)
                    phrasePart['type'] = 'plain-text'
                    phrasePart['value'] = [data]
                    if i == 0:
                        structure = [phrasePart]
                    else:
                        structure.append(phrasePart)
            data = ''
        elif char == '&':
            # if first & had been found and last & is found --> save column entity
            if foundFirstAmpersand:
                phrasePart['order'] = len(structure)
                phrasePart['type'] = 'value'
                phrasePart['value'] = [item.strip() for item in data.split(',')]
                if i == 0:
                    structure = [phrasePart]
                else:
                    structure.append(phrasePart)
                # reset value to false
                foundFirstAmpersand = False
            else:
                # if is first percentaje set value to True
                foundFirstAmpersand = True
                # save data if previous data is a simple word
                if data != '' and isSimpleWord:
                    isSimpleWord = False
                    phrasePart['order'] = len(structure)
                    phrasePart['type'] = 'plain-text'
                    phrasePart['value'] = [data]
                    if i == 0:
                        structure = [phrasePart]
                    else:
                        structure.append(phrasePart)
            data = ''
        else:
            data = data + char
            if not foundFirstAmpersand and not foundFirstPercentage:
                isSimpleWord = True
    return structure

'''
def createPhraseStructure(phrase):
    foundFirstPercentage = False
    foundFirstAmpersand = False
    isSimpleWord = False
    structure = []
    data = ''
    for i, char in enumerate(phrase):
        if char == '%':
            # si se ha encontrado el primer y ultimo % resetear data
            if foundFirstPercentage:
                eWord = copy.deepcopy(entityWord)
                eWord['text'] = data
                eWord['alias'] = "columns_select_" + tableName
                eWord['meta'] = "@columns_select_" + tableName
                if i == 0:
                    structure = [eWord]
                else:
                    structure.append(eWord)
                # reset value to false
                foundFirstPercentage = False
            else:
                # if is first percentaje set value to True
                foundFirstPercentage = True
                # guardar data si lo anterior era una palabra normal
                if data != '' and isSimpleWord:
                    isSimpleWord = False
                    word = copy.deepcopy(simpleWord)
                    word['text'] = data
                    if i == 0:
                        structure = [word]
                    else:
                        structure.append(word)

            data = ''
        elif char == '&':
            # si se ha encontrado el primer y ultimo % resetear data
            if foundFirstAmpersand:
                eWord = copy.deepcopy(entityWord)
                eWord['text'] = data
                if i == 0:
                    structure = [eWord]
                else:
                    structure.append(eWord)
                # reset value to false
                foundFirstAmpersand = False
            else:
                # if is first percentaje set value to True
                foundFirstAmpersand = True
                # guardar data si lo anterior era una palabra normal
                if data != '' and isSimpleWord:
                    isSimpleWord = False
                    word = copy.deepcopy(simpleWord)
                    word['text'] = data
                    if i == 0:
                        structure = [word]
                    else:
                        structure.append(word)
            data = ''
        else:
            data = data + char
            if not foundFirstAmpersand and not foundFirstPercentage:
                isSimpleWord = True
    return structure
'''
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
    global idIntents
    fileName =  pathToWrite + '/intents/' + table['table_name']
    # create intents for query with where
    phrasesWhere = createTrainingPhrases(PhrasesPath, True)
    if phrasesWhere:
        writeToFile(phrasesWhere, fileName + '_where_usersays_en.json')
        createIntentFile(pathToWrite, table['table_name'] + '_where', idIntents)
        idIntents = idIntents + 1

    # create intents for query without where
    phrasesNoWhere = createTrainingPhrases(PhrasesPath, False)
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


#read csv and save a sample for phrases
def readCsvAndSaveInMemory(file, fields, thereIsHead):
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


# find a column in given list with an order
def findFieldWithOrder(order, list):
    for f in list:
        if f['order'] == order:
            return f
    return None

# clear data from invalid character
# invalid characters will be changed by specified character
def clearData(string, charToPut):
    string = list(string)
    for i in range(0, len(string)):
        if not string[i] in allowedChar:
            string[i] = charToPut
    string = ''.join(string)
    return string

#def inferTypesOfRows():model['plaques'][0]['plaques']


# create "the [column] of [value]"
# create "the [column] with [value]"
# create "the [column] with [column] [value]"
# create "the [column] if [column] [value]"
def createType2Phrases(sentences):
    global idCount
    #sentences = []
    simpleWord1 = copy.deepcopy(simpleWord)
    simpleWord1['text'] = "The "
    simpleWord2 = copy.deepcopy(simpleWord)
    simpleWord2['text'] = " of "
    simpleWord3 = copy.deepcopy(simpleWord)
    simpleWord3['text'] = " with "
    for c1 in rows:
        entityWord1 = copy.deepcopy(entityWord)
        entityWord1['text'] = c1[0]
        entityWord1['alias'] = "columns_select_" + tableName
        entityWord1['meta'] = "@columns_select_" + tableName
        for c2 in rows:
            if c2[0] != c1[0]:
                for i, val in enumerate(c2):
                    if i > 2:
                        entityWordWithValue = copy.deepcopy(entityWord)
                        entityWordWithValue['text'] = val
                        entityWordWithValue['alias'] = c2[2]
                        entityWordWithValue['meta'] = "@" + c2[1]
                        # for "the [column] of [value]"
                        copySentence1 = copy.deepcopy(sentence)
                        copySentence1['id'] = idCount
                        idCount = idCount + 1
                        copySentence1['data'] = [simpleWord1,entityWord1, simpleWord2, entityWordWithValue]
                        # for "the [column] with [value]"
                        copySentence2 = copy.deepcopy(sentence)
                        copySentence2['id'] = idCount
                        idCount = idCount + 1
                        copySentence2['id'] = [simpleWord1,entityWord1, simpleWord3, entityWordWithValue]
                        # for "the [column] with [column] [value]"
                        copySentence3 = copy.deepcopy(sentence)
                        copySentence3['id'] = idCount
                        idCount = idCount + 1
                        copySentence3['data'] = [simpleWord1,entityWord1, simpleWord3, entityWordWithValue]
                        # for "the [column] of [column] [value]"

                        sentences.append(copySentence1)
                        sentences.append(copySentence2)

    #print(json.dumps(Sentences, indent=4, sort_keys=True))
    #return elements


# create phrases with "all [column]"
def createType1Phrases():
    global idCount
    copySimpleWord = copy.deepcopy(simpleWord)
    copySimpleWord['text'] = "All "
    sentences = []
    index = 0
    for c in rows:
        copyEntityWord = copy.deepcopy(entityWord)
        copySentence = copy.deepcopy(sentence)
        copyEntityWord['text'] = c[0]
        copyEntityWord['alias'] = "columns_select_"  + tableName
        copyEntityWord['meta'] = "@columns_select_" + tableName
        copySentence['id'] = idCount
        idCount = idCount + 1
        copySentence['data'] = [copySimpleWord,copyEntityWord]
        if index == 0:
            sentences = [copySentence]
        else:
            sentences.append(copySentence)
        index = index + 1
    #print(json.dumps(Sentences, indent=4, sort_keys=True))
    return sentences

# write json to a file
def writeToFile(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def encodeUTF8(a):
  for list in a:
    return [x.encode('utf-8') for x in list]

#def formatNumbersAndDates():

def readModelFromFile(file):
    model = None
    with open(file, 'r') as f:
        model = json.load(f)
    return model

# main
def main():

    # read model from file json
    # this model contains db schema
    model = readModelFromFile("./schema2.json")

    # for each table --> create entities and intents
    for table in model['tables']:
        # read data from CSV
        global rows
        rows = readCsvAndSaveInMemory("../data/Placas_memoriademadrid.csv", table['fields'], True)
        createIntents("./phrases", "./v3", table)

        createAllEntitiesFiles(table['table_name'], table['fields'])



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
