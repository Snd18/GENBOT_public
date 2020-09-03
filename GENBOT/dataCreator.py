import csv
import copy

class DataCreator:

    # data to work
    table = {
        "table_name" : "",
        "fields" : []
    }
    field = {
        "field_name" : "",
        "entity_name" : "",
        "entity_type" : "",
        "values" : [],
        "synonyms" : []
    }

    def __init__(self, sample):
        self.sample = sample

    def getSampleAndStructuredData(self, file, thereIsHead, tableStructure):
        '''
        Reads a sample of rows from csv and creates structured data with column data and info for work.
        '''
        # get a sample of rows
        rows = self.__readCsvAndGetRows(file, thereIsHead)
        # get structured data to work
        structuredData = self.__getStructuredData(rows, tableStructure)
        return structuredData

    def __getStructuredData(self, rows, tableStructure):
        '''
        Return a structured data for work given rows of values and the structure of table.
        '''
        # traspose data --> rows into columns
        columns = []
        for i in range(0, len(rows[1])):
            col = [rows[j][i] for j in range(0, self.sample-1)]
            if i == 0:
                columns = [col]
            else:
                columns.append(col)

        # create the structure of data
        self.table['table_name'] = str(tableStructure['table_name'])
        fields = [self.__constructField(item, str(tableStructure['table_name']), columns) for item in tableStructure['fields']]
        self.table['fields'] = fields
        return self.table

    def __constructField(self, item, tableName, values):
        '''
        Construct a field element for global table map.
        '''
        entity_type = ""
        # copy de structure of a field element
        fieldToReturn = copy.deepcopy(self.field)
        # complete all atributes of a field
        fieldToReturn['field_name'] = str(item['field_name'])
        fieldToReturn['entity_name'] = tableName + '_' + str(item['field_name'])
        fieldToReturn['synonyms'] = item['synonyms']
        if item['entity_type'] == 'None':
            entity_type = '@' + fieldToReturn['entity_name']
        else:
            entity_type = str('@' + item['entity_type'])
        fieldToReturn['entity_type'] = entity_type
        fieldToReturn['values'] = values[item['order']]

        return fieldToReturn


    def __readCsvAndGetRows(self, file, thereIsHead):
        '''
        Read csv and return a sample values for training phrases.
        '''
        with open(file) as File:
            reader = csv.reader(File)
            # position to stop reading
            stop = self.sample
            # if there is a head with columns names in csv --> get one more csv line
            if thereIsHead:
                stop = self.sample + 1
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
