import json
import copy
import random
import itertools
from itertools import chain, combinations
from utils import utils as write

class IntentCreator:

    # structure for phrases
    phraseStructure = {
        "order" : 0,
        "type" : "",
        "table": "",
        "value" : []
    }



    def createIntents(self):
        '''
        Create all intents files for Dialogflow agent.
        Recieve a initial id and return the last id used.
        '''
        id = 0

        for table in self.db.tables:
            fileName =  self.rootFolder + '/intents/' + table.name

            # create intents for query with where
            phrasesWhere = self.__createTrainingPhrases(True, table)
            # if there are phrases with "where":
            if phrasesWhere:
                self.__writeToFile(phrasesWhere, fileName + '_where_usersays_en.json')
                self.__createIntentFile(table.name + '_where', id)
                id = id + 1

            # create intents for query without where
            phrasesNoWhere = self.__createTrainingPhrases(False, table)
            # if there are phrases without "where":
            if phrasesNoWhere:
                self.__writeToFile(phrasesNoWhere, fileName + '_nowhere_usersays_en.json')
                self.__createIntentFile(table.name + '_nowhere', id)
                id = id + 1
            # return the last id used
        #return idIntents

    def __createIntentFile(self, fileName, id):
        '''
        Create a file for intent given a name, id and path.
        '''
        file = copy.deepcopy(self.intent)
        file['id'] = id
        file['name'] = fileName
        self.__writeToFile(file, self.rootFolder + '/intents/' + fileName + '.json')


    def __createTrainingPhrases(self, ithasValues, table):
        '''
        Create training phrases for intents according to a model in especified file.
        Depending on the "ithasValues" value (True or False), it will be created
        training phrases with or without values.
        '''
        # read from file
        # model phrases
        phrases = self.__readTrainPhrases(self.phrasesPath)
        # choose model phrases from file with or without "where"
        phrases = self.__phrasesFilter(ithasValues, phrases)
        # create list with training phrases
        phrasesJson = [self.__createPhrasesJson(p, table) for p in phrases]
        # join in a unique list
        phrasesJson = [j for i in phrasesJson for j in i]
        #phrasesJson = list(itertools.chain(*phrasesJson))
        #print(phrasesJson)
        return phrasesJson

    def __createPhrasesJson(self, phrase, table):
        '''
        Create training phrases to insert in json files.
        '''
        phraseStructure = self.__createPhraseStructure(phrase)
        return self.__createMultiplePhrasesWithStructure(phraseStructure, table)

    def __phrasesFilter(self, hasValue, phrases):
        if hasValue:
            phrasesWithFilter = [p for p in phrases if self.__hasValues(p)]
        else:
            phrasesWithFilter = [p for p in phrases if not self.__hasValues(p)]

        return phrasesWithFilter

    def __hasValues(self, phrase):
        hasValues = False
        for letter in phrase:
            if letter == '&':
                hasValues = True
        return hasValues


    def __isColumnNameEntity(self, word):
        alias = word.get('alias')
        if alias and 'columns_select' in alias:
            return True
        else:
            return False

    def __isValueEntity(self, word):
        alias = word.get('alias')
        if alias  != None and alias == "":
            return True
        else:
            return False

    def __createMultiplePhrasesWithStructure(self, structure, table):
        '''
        Genere all combinations of values from structure to make training phrases.
        Make all training phrases with the combination above.
        '''
        combinedValues = self.__combineValuesAndColumns(structure)

        #phraseList = createPhrases(combinedValues)
        #print(combinedValues)
        returnPhrases = []
        for i, t in enumerate(combinedValues):
            metadata = copy.deepcopy(self.sentence)
            metadata['id'] = i
            metadata['data'] = self.__createPhrase(t, structure, table)
            returnPhrases.append(metadata)
        #return [createPhrase(tuple, structure) for tuple in combinedValues]
        return returnPhrases

    def __createPhrase(self, tupleValues, structure, table):
        '''
        Create one training phrase with tuple of values and structure.
        '''
        index = 0
        # we consider that the orden of elements in structure is the correct for training phrases.
        sentence = []
        for i, word in enumerate(structure):
            if word['type'] == 'value':
                for value in tupleValues[index]:
                    sentence.append(self.__createValue(value, table))
                    sentence.append(self.__createPlainText(', '))
                sentence.pop()
                index += 1
            elif word['type'] == 'column_where':
                sentence.append(self.__createColumns('columns_where', tupleValues[index]))
                index += 1
            elif word['type'] == 'column_select':
                sentence.append(self.__createColumns('columns_select', tupleValues[index]))
                index += 1
            elif word['type'] == 'plain-text':
                sentence.append(self.__createPlainText(word['value'][0]))
        print(sentence)
        #for word in phrase:
        #    if word
        return sentence

    def __createValue(self, value, table):
        phrasePart = copy.deepcopy(self.entityWord)
        phrasePart['text'] = self.__getRandomValue(value, table)
        phrasePart['meta'] = self.__getMetaValue(table, value)
        if 'sys.' in phrasePart['meta']:
            phrasePart['alias'] = phrasePart['meta'][5:]
        else:
            phrasePart['alias'] = table.name + '_' + value
        return phrasePart

    def __createColumns(self, columns, value):
        phrasePart = copy.deepcopy(self.entityWord)
        phrasePart['text'] = value
        phrasePart['alias'] = columns
        phrasePart['meta'] = '@' + columns
        return phrasePart

    def __createPlainText(self, text):
        phrasePart = copy.deepcopy(self.simpleWord)
        phrasePart['text'] = text
        return phrasePart

    def __getMetaValue(self, table, fieldname):
        '''
        Get meta info for Dialogflow from schema given a column.
        '''
        meta = ''
        for field in table.fields:
            print(field.name)
            print(fieldname)
            if field.name.lower() == fieldname.lower():
                if field.entity_meta == 'None':
                    meta = '@' + field.tablename.lower() + '_' + field.name.lower()
                else:
                    meta = '@' + field.entity_meta
        return meta

    def __getRandomValue(self, column, table):
        '''
        Get random value from sample data given a table and column.
        '''
        value = ""
        for field in table.fields:
            if field.name == column:
                max = len(field.values) - 1
                randomIndex = random.randint(1,max)
                value = field.values[randomIndex]
        return value

    def __createValuesWithNameEntity(self, values):
        #del values[0:4]
        listFinal = []
        for i, row in enumerate(values):
            nameEntity = row[0]
            del row[0:2]
            list = [[nameEntity, value] for value in row]
            listFinal.append(list)
        #print(values)
        return listFinal

    def __listToString(self, list):
        '''
        With a given list return another with all elements cast to string.
        Method used to remove unicode annotation.
        '''
        return [str(item) for item in list]

    def __powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))[1:]


    def __combineValuesAndColumns(self, structure):
        '''
        Return a list with all posible values and columns names combinations given a structure.
        '''
        power = []
        listToCombine = [part['value'] for part in structure if part['type'] != 'plain-text']
        if len(listToCombine) == 1:
            #return [[item] for item in listToCombine[0]]
            power.append([listToCombine[0]])
        else:
            for item in listToCombine:
                if len(item) > 1:
                    item = self.__powerset(item)
                power.append(item)
        final = [comb for comb in itertools.product(*power)]
        print(final)
        return final

    def __createPhraseStructure(self, phrase):
        '''
        Creates a structure for making training phrases given a example phrase.
        Return phrase structure.
        '''
        foundFirstPercentage = False
        foundFirstAmpersand = False
        isSimpleWord = False
        structure = []
        data = ''
        for i, char in enumerate(phrase):
            phrasePart = copy.deepcopy(self.phraseStructure)
            if char == '%':
                # if first % had been found and last % is found --> save column entity
                if foundFirstPercentage:
                    phrasePart['order'] = len(structure)
                    if 'select' in data.split(':')[:5]:
                        phrasePart['type'] = 'column_select'
                    else:
                        phrasePart['type'] = 'column_where'
                    phrasePart['value'] = [self.__clearColumnsValues(item.strip()) for item in data.split(',')]
                    phrasePart['table'] = data.split(':')[1]
                    # save phrase part into array
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
                        structure.append(phrasePart)
                data = ''
            elif char == '&':
                # if first & had been found and last & is found --> save column entity
                if foundFirstAmpersand:
                    phrasePart['order'] = len(structure)
                    phrasePart['type'] = 'value'
                    phrasePart['value'] = [self.__clearColumnsValues(item.strip()) for item in data.split(',')]
                    phrasePart['table'] = data.split(',')[0].split(':')[1]
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
                        structure.append(phrasePart)
                data = ''
            else:
                data = data + char
                if not foundFirstAmpersand and not foundFirstPercentage:
                    isSimpleWord = True
        print(structure)
        return structure

    def __clearColumnsValues(self, item):
        '''
        the input element is split by the character ':'
        Return then the first element.
        '''
        return item.split(':')[0]


    def __isComment(self, line):
        if line[0] == '#':
            return True
        else:
            return False

    def __readTrainPhrases(self, file):
        f = open(file, "r")
        lines = []
        with open(file) as f:
            content = f.readlines()
            # scape comments
            lines = [line for line in content if not self.__isComment(line)]
            #lines = [line.strip() for line in content]
            #lines = [str(line) for line in f]
        return lines
