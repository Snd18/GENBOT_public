

class Request():

    def __init__(self, req):
        self.req = req

    @property
    def req(self):
        return self.__req

    @property
    def columns_select(self):
        return self.__getColumnsSelect()

    @property
    def fieldMap(self):
        return self.__getFieldMap()

    @property
    def valueMap(self):
        return self.__getValueMap()

    @property
    def lat(self):
        return self.__getLat()

    @property
    def long(self):
        return self.__getLon()

    @property
    def extrainfo(self):
        return self.__getExtrainfo()

    @property
    def command(self):
        return self.__getComand()

    @property
    def intent(self):
        return self.__getIntentName()

    @property
    def typeSimpleGraph(self):
        return self.__getTypeSimpleGraph()

    @property
    def typeComplexGraph(self):
        return self.__getTypeComplexGraph()

    @property
    def user(self):
        return self.__getUser()

    @property
    def parameters(self):
        return self.__getParameters()

    @property
    def idFromReq(self):
        return self.__getIdFromReq()

    @property
    def tablename(self):
        return self.__getTableName()

    @property
    def databasename(self):
        return self.__getDatabaseName()

    @property
    def simpleGrapField(self):
        return self.__getSimpleGrapField()

    @property
    def graphFields(self):
        return self.__getGraphFields()

    @req.setter
    def req(self, req):
        self.__req = req

    def __getFieldMap(self):
        '''
        Return the value of map field.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('fieldname'):
            value = self.req.get('queryResult').get('parameters').get('fieldname')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('fieldname'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('fieldname')
        return value

    def __getColumnsSelect(self):
        '''
        Return columns select values
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('columns_select'):
            value = self.req.get('queryResult').get('parameters').get('columns_select')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('columns_select'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('columns_select')
        return value
        
    def __getValueMap(self):
        '''
        Return the value of map field.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('valueMap'):
            value = self.req.get('queryResult').get('parameters').get('valueMap')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('valueMap'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('valueMap')
        return value

    def __getLat(self):
        '''
        Return the value of map field.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('latitude'):
            value = self.req.get('queryResult').get('parameters').get('latitude')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('latitude'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('latitude')
        return value

    def __getLon(self):
        '''
        Return the value of map field.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('longitude'):
            value = self.req.get('queryResult').get('parameters').get('longitude')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('longitude'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('longitude')
        return value


    def __getExtrainfo(self):
        '''
        Return the value of map field.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('extraInfo'):
            value = self.req.get('queryResult').get('parameters').get('extraInfo')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('extraInfo'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('extraInfo')
        return value

    def __getComand(self):
        '''
        Return the command from request.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('commands'):
            value = self.req.get('queryResult').get('parameters').get('commands')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('commands'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('commands')
        return value

    def __getIntentName(self):
        '''
        Return the name of intent from request.
        '''
        value = None
        if self.req.get('queryResult').get('intent').get('displayName'):
            value = self.req.get('queryResult').get('intent').get('displayName')
        return value

    def __getTypeSimpleGraph(self):
        '''
        Return the type of one var graph.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('simple_graph'):
            value = self.req.get('queryResult').get('parameters').get('simple_graph')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('simple_graph'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('simple_graph')
        return value

    def __getTypeComplexGraph(self):
        '''
        Return the type of two var graph.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('complex_graph'):
            value = self.req.get('queryResult').get('parameters').get('complex_graph')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('complex_graph'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('complex_graph')
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

    def __getParameters(self):
        '''
        Return the parameters from request.
        '''
        value = None
        if self.req['queryResult']['parameters']:
            value = self.req['queryResult']['parameters']
        return value

    def __getIdFromReq(self):
        '''
        Return the image id from request.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('idImage'):
            value = str(int(self.req.get('queryResult').get('parameters').get('idImage')))
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('idImage'):
                    value = str(int(self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('idImage')))
        return value

    def __getTableName(self):
        '''
        Return the table name from request.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('tablename'):
            value = self.req.get('queryResult').get('parameters').get('tablename')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('tablename'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('tablename')
        return value

    def __getDatabaseName(self):
        '''
        Return the database name from request.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('databasename'):
            value = self.req.get('queryResult').get('parameters').get('databasename')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('databasename'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('databasename')
        return value

    def __getSimpleGrapField(self):
        '''
        Return the field to make the graph with one variable.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('columns_select'):
            value = self.req.get('queryResult').get('parameters').get('columns_select')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('columns_select'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('columns_select')
        return value

    def __getGraphFields(self):
        '''
        Return the field2 to make the graph.
        '''
        value = None
        if self.req.get('queryResult').get('parameters').get('columns_select'):
            value = self.req.get('queryResult').get('parameters').get('columns_select')
        else:
            if self.req.get('queryResult').get('outputContexts'):
                if self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('columns_select'):
                    value = self.req.get('queryResult').get('outputContexts')[0].get('parameters').get('columns_select')
        return value
