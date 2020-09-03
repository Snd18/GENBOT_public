import json
import copy
import io
import entityCreator as ec
import dataCreator as dc
import intentCreator as ic

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

model = None

allowedChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','_','1','2','3','4','5','6','7','8','9','0']

# table name
tableName = "plaques"

# global id for phrases
idCount = 0

# global id for intents
idIntents = 0

# number of rows to get from csv
sample = 6



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



def readModelFromFile(file):
    '''
    Return a model read from a json file.
    '''
    model = None
    with open(file, 'r') as f:
        model = json.load(f)
    return model


# main
def main():
    lastId = 0
    csvPath = "../data/Placas_memoriademadrid.csv"
    trainingPhrasesPath = "./inputs/phrases"
    rootFolder = "./outputs/v3"
    headers = True
    entityCreator = ec.EntityCreator(rootFolder)
    dataCreator = dc.DataCreator(sample)
    intentCreator = ic.IntentCreator()
    # read model from file json
    # this model contains db schema
    global model
    model = readModelFromFile("./inputs/schema_v2.json")

    # for each table --> create entities and intents
    for t in model['tables']:
        # read data from CSV and save a sample
        tabledata = dataCreator.getSampleAndStructuredData(csvPath, headers, t)
        print(tabledata)
        lastId = intentCreator.createIntents(trainingPhrasesPath, rootFolder, tabledata, lastId)
        entityCreator.createAllEntitiesFiles(t['table_name'], tabledata['fields'])


if __name__ == '__main__':
   main()
