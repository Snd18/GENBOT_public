from utils import utils


class AskComplexGraph():

    filepath = "../outputs/v4/intents/"

    name = 'Ask for complex graph'

    def __init__(self, database, table):
        self.database = database
        self.table = table

    @property
    def intent(self):
        intent = {
        "id":"7c308982-f0d2-4129-b5d4-5f01d21545b8",
        "name":"Ask for complex graph",
        "auto":True,
        "contexts":[

        ],
        "responses":[
        {
        "resetContexts":False,
        "affectedContexts":[
        {
        "name":"Twovargraph-followup",
        "parameters":{

        },
        "lifespan":2
        }
        ],
        "parameters":[
        {
        "id":"3bb0df88-f36d-42eb-be60-08c021ef469d",
        "required":True,
        "dataType":"@columns_select",
        "name":"columns_select",
        "value":"$columns_select",
        "promptMessages":[

        ],
        "noMatchPromptMessages":[

        ],
        "noInputPromptMessages":[

        ],
        "outputDialogContexts":[

        ],
        "isList":True
        },
        {
        "id":"26e56b0a-03b7-4ceb-8322-5b4d9089d231",
        "required":False,
        "dataType":"",
        "name":"tablename",
        "value":self.table,
        "promptMessages":[

        ],
        "noMatchPromptMessages":[

        ],
        "noInputPromptMessages":[

        ],
        "outputDialogContexts":[

        ],
        "isList":False
        },
        {
        "id":"ba50e724-051b-4c8d-aacf-23b97fea00f0",
        "required":False,
        "dataType":"",
        "name":"databasename",
        "value":self.database,
        "promptMessages":[

        ],
        "noMatchPromptMessages":[

        ],
        "noInputPromptMessages":[

        ],
        "outputDialogContexts":[

        ],
        "isList":False
        }
        ],
        "messages":[

        ],
        "defaultResponsePlatforms":{

        },
        "speech":[

        ]
        }
        ],
        "priority":500000,
        "webhookUsed":True,
        "webhookForSlotFilling":False,
        "fallbackIntent":False,
        "events":[

        ],
        "conditionalResponses":[

        ],
        "condition":"",
        "conditionalFollowupEvents":[

        ]
        }
        return intent

    @property
    def usersays(self):
        us = [
        {
        "id":"41f24594-9c05-4797-9c02-bdfef39b8a2e",
        "data":[
        {
        "text":"graph ",
        "userDefined":False
        },
        {
        "text":"one",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":", ",
        "userDefined":False
        },
        {
        "text":"two",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":", ",
        "userDefined":False
        },
        {
        "text":"three",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"58ed5d98-560c-4758-88ab-c50e5fd627ac",
        "data":[
        {
        "text":"graph ",
        "userDefined":False
        },
        {
        "text":"one",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"5063647f-b26c-419a-bb2f-af018a191dec",
        "data":[
        {
        "text":"A graph with ",
        "userDefined":False
        },
        {
        "text":"one",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":False
        },
        {
        "text":", ",
        "userDefined":False
        },
        {
        "text":"two",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":" and ",
        "userDefined":False
        },
        {
        "text":"three",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"9b9bc170-b480-4e56-8e22-fa6a3976bc06",
        "data":[
        {
        "text":"A graph with ",
        "userDefined":False
        },
        {
        "text":"one",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":" and ",
        "userDefined":False
        },
        {
        "text":"two",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"15f1fa59-af6a-4bdc-b122-ba787d70aae4",
        "data":[
        {
        "text":"A graph with ",
        "userDefined":False
        },
        {
        "text":"one",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":False
        },
        {
        "text":", ",
        "userDefined":False
        },
        {
        "text":"two",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":False
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"34ec4914-f864-4d2d-9c9d-cb6f042e78c1",
        "data":[
        {
        "text":"A graph with ",
        "userDefined":False
        },
        {
        "text":"one",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":False
        },
        {
        "text":", ",
        "userDefined":False
        },
        {
        "text":"two",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":", ",
        "userDefined":False
        },
        {
        "text":"three",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"9c8e394c-7a00-42d1-8a56-f51833413f53",
        "data":[
        {
        "text":"graph",
        "userDefined":False
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"b6e5447b-0460-4280-989e-efa128fd2ef4",
        "data":[
        {
        "text":"localizacion_coordenada_y",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":" vs ",
        "userDefined":False
        },
        {
        "text":"localizacion_coordenada_y",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"07de519b-3f1f-4e92-84a5-5df1647bc275",
        "data":[
        {
        "text":"A graph with ",
        "userDefined":False
        },
        {
        "text":"direccion_coordenada_x",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":" vs ",
        "userDefined":False
        },
        {
        "text":"direccion_coordenada_y",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"f1b88e4d-420e-47df-ad71-d43ceb637657",
        "data":[
        {
        "text":"I want a graph with ",
        "userDefined":False
        },
        {
        "text":"direccion_coordenada_x",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":" vs ",
        "userDefined":False
        },
        {
        "text":"direccion_coordenada_y",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"01e193cd-906e-4bde-a574-ba08b768d4de",
        "data":[
        {
        "text":"view graph with ",
        "userDefined":False
        },
        {
        "text":"direccion_coordenada_x",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        },
        {
        "text":" vs ",
        "userDefined":False
        },
        {
        "text":"direccion_coordenada_y",
        "alias":"columns_select",
        "meta":"@columns_select",
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        }
        ]
        return us

    @property
    def database(self):
        return self.__database

    @property
    def table(self):
        return self.__table

    @database.setter
    def database(self, database):
        self.__database = database

    @table.setter
    def table(self, table):
        self.__table = table

    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
        utils.writeToFile(self.usersays, self.filepath + self.name + '_usersays_en.json')
