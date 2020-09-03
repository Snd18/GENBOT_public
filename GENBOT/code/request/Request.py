from utils import utils


class Request():

    def __init__(self, req):
        self.req = req

    @property
    def req(self):
        return self.__req

    @property
    def dbname(self):
        return self.__getdbname()

    @property
    def csv(self):
        return self.__getCsv()

    @property
    def synonyms(self):
        return self.__getSynonyms()

    @property
    def fieldname(self):
        return self.__getFieldName()

    @property
    def tablename(self):
        return self.__getTableName()

    @property
    def dbType(self):
        return self.__getDBType()

    @property
    def user(self):
        return self.__getUser()

    @property
    def dfType(self):
        return self.__getDFType()

    @property
    def intent(self):
        return self.__getIntent()

    @property
    def coordinate(self):
        return self.__getCoordinate()

    @property
    def extraInfo(self):
        return self.__getExtraInfo()

    @req.setter
    def req(self, req):
        self.__req = req

    def __getdbname(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('db_name'):
            value = str(self.req.get('queryResult').get('parameters').get('db_name'))
        return utils.clearData(value, '')

    def __getCsv(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('csv_path'):
            value = str(self.req.get('queryResult').get('parameters').get('csv_path'))
        return value

    def __getSynonyms(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('synonyms'):
            synonyms = self.req.get('queryResult').get('parameters').get('synonyms')
            value = [str(item.strip()) for item in synonyms]
        return value

    def __getFieldName(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('fieldname'):
            value = self.req.get('queryResult').get('parameters').get('fieldname')
        elif self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('fieldname'):
            value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('fieldname')
        return utils.clearData(value, '')

    def __getTableName(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('tablename'):
            value = self.req.get('queryResult').get('parameters').get('tablename')
        elif self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('tablename'):
            value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('tablename')
        return utils.clearData(value, '')

    def __getDBType(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('db_type'):
            value = str(self.req.get('queryResult').get('parameters').get('db_type'))
        return value

    def __getDFType(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('df_type'):
            value = str(self.req.get('queryResult').get('parameters').get('df_type'))
        return value

    def __getUser(self):
        value = 'dialogflow'
        if self.req.get('originalDetectIntentRequest').get('payload').get('data').get('from'):
            value = self.req.get('originalDetectIntentRequest').get('payload').get('data').get('from').get('username')
        elif self.req.get('originalDetectIntentRequest').get('payload').get('callback_query'):
            value = self.req.get('originalDetectIntentRequest').get('payload').get('callback_query').get('from').get('username')
        elif self.req.get('originalDetectIntentRequest').get('payload').get('data').get('callback_query').get('from').get('username'):
            value = self.req.get('originalDetectIntentRequest').get('payload').get('data').get('callback_query').get('from').get('username')

        return value

    def __getIntent(self):
        '''
        Return the name of intent from request.
        '''
        value = None
        if self.req.get('queryResult').get('intent').get('displayName'):
            value = self.req.get('queryResult').get('intent').get('displayName')
        return value

    def __getCoordinate(self):
        value = None
        if self.req.get('queryResult').get('parameters').get('coordinate'):
            value = self.req.get('queryResult').get('parameters').get('coordinate')
        elif self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('coordinate'):
            value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('coordinate')
        return utils.clearData(value, '')

    def __getExtraInfo(self):
        value = ' '
        if self.req.get('queryResult').get('parameters').get('extraInfo'):
            value = self.req.get('queryResult').get('parameters').get('extraInfo')
        elif self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('extraInfo'):
            value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('extraInfo')
        return value
