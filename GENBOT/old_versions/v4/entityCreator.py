import copy
import json

class EntityCreator:

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

    def __init__(self, rootFolder):
        self.rootFolder = rootFolder

    def createAllEntitiesFiles(self, tableName, fieldList):
        '''
        Create all entities files: [fieldName].json and [fieldName]_entries_en.json.
        Each entity has two json files.
        '''
        # control id for entities
        id = 0
        # create entities for each field/column in data
        for i, field in enumerate(fieldList):
            if not 'sys.' in field['entity_type']:
                self.createEntityFile(field, tableName, i, True)
                self.__createEntityEntriesFile(tableName, field)
                id = i
        # create entity [columns_select_tablename]
        id = id + 1
        self.__createEntitySelectFile(tableName, id, False)
        self.__createEntityEntriesSelectFile(tableName, fieldList)
        # create entity [columns_where_tablename]
        id = id + 1
        self.__createEntityWhereFile(tableName, id, False)
        self.__createEntityEntriesWhereFile(tableName, fieldList)


    def createEntityFile(self, field, tableName, id, automatedExpansion):
        '''
        Create entity file: [tablename_columnName].json.
        '''
        filename = self.rootFolder + "/entities/" + tableName + "_" + field['field_name'] + ".json"
        e = copy.deepcopy(self.entity)
        e['id'] = id
        e['name'] = tableName + "_" + field['field_name']
        e['automatedExpansion'] = automatedExpansion
        self.__writeToFile(e, filename)


    def __createEntityEntriesFile(self, tableName, field):
        '''
        Create entity file: [tablename_columnName]_entries_en.json
        '''
        filename = self.rootFolder + "/entities/" + tableName + "_" + field['field_name'] + "_entries_en.json"
        '''
        global table
        for field in table['fields']:
            if field['field_name'] == item['field_name']:
                entries = [self.__createEntries(value, value) for value in field['values']]
                self.__writeToFile(entries, filename)
                return
        '''
        entries = [self.__createEntries(value, [value]) for value in field['values']]
        self.__writeToFile(entries, filename)

    def __createEntries(self, value, synonyms):
        '''
        Create a entry for [name]_entries_en.json files.
        Value is a string.
        Synonyms are a list of synonyms.
        '''
        e = copy.deepcopy(self.entity_entry)
        e['value'] = value
        e['synonyms'] = synonyms
        return e

    def __createEntitySelectFile(self, tableName, id, automatedExpansion):
        '''
        Create entity file: columns_select.json
        '''
        #filename = "./v3/entities/columns_select_" + tablename + ".json"
        filename = self.rootFolder + "/entities/columns_select.json"
        e = copy.deepcopy(self.entity)
        e['id'] = id
        #e['name'] = "columns_select_" + tablename
        e['name'] = "columns_select"
        e['automatedExpansion'] = automatedExpansion
        self.__writeToFile(e, filename)


    def __createEntityEntriesSelectFile(self, tableName, fieldList):
        '''
        Create entity file: columns_select_entries_en.json.
        '''
        #filename = "./v3/entities/columns_select_" + tablename + "_entries_en.json"
        filename = self.rootFolder + "/entities/columns_select_entries_en.json"
        fields = [self.__createEntries(field['field_name'], field['synonyms']) for field in fieldList]
        self.__writeToFile(fields, filename)


    def __createEntityWhereFile(self, tableName, id, automatedExpansion):
        '''
        Create entity file: columns_where.json.
        '''
        #filename = "./v3/entities/columns_where_" + tablename + ".json"
        filename = self.rootFolder + "/entities/columns_where.json"
        e = copy.deepcopy(self.entity)
        e['id'] = id
        #e['name'] = "columns_where_" + tablename
        e['name'] = "columns_where"
        e['automatedExpansion'] = automatedExpansion
        self.__writeToFile(e, filename)


    def __createEntityEntriesWhereFile(self, tableName, fieldList):
        '''
        Create entity file: columns_where_entries_en.json.
        '''
        #filename = "./v3/entities/columns_where_" + tablename + "_entries_en.json"
        filename = self.rootFolder + "/entities/columns_where_entries_en.json"
        fields = [self.__createEntries(field['field_name'], field['synonyms']) for field in fieldList]
        self.__writeToFile(fields, filename)


    def __writeToFile(self, data, filename):
        '''
        Write json to a file
        '''
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
