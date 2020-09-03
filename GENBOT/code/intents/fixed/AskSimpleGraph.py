from utils import utils


class AskSimpleGraph():

    filepath = "../outputs/v4/intents/"

    name = 'Ask for simple graph'

    def __init__(self, database, table):
        self.database = database
        self.table = table

    @property
    def intent(self):
        intent = {
            "id":"e11b8917-20e9-4a82-b922-2736f8cdfc09",
            "name":"Ask for simple graph",
            "auto":True,
            "contexts":[

            ],
            "responses":[
                {
                    "resetContexts":False,
                    "affectedContexts":[
                        {
                            "name":"Onevargraph-followup",
                            "parameters":{

                            },
                            "lifespan":2
                        }
                    ],
                    "parameters":[
                        {
                            "id":"14fdfc18-8de5-4e59-9f88-671f7c860267",
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
                            "isList":False
                        },
                        {
                            "id":"cec2ff71-e354-44e8-b778-380ed3d985f1",
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
                            "id":"6ca4e741-d589-4d00-b40d-8ba5a06936bb",
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
                        {
                            "type":0,
                            "lang":"en",
                            "condition":"",
                            "speech":"ghhfghf"
                        }
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
        usersays = [
      {
        "id": "27aaa212-aed5-41fe-9f84-75b25500f6a1",
        "data": [
          {
            "text": "one",
            "meta": "@sys.ignore",
            "userDefined": False
          },
          {
            "text": " var graph",
            "userDefined": False
          }
        ],
        "isTemplate": False,
        "count": 0,
        "updated": 0
      },
      {
        "id": "6c7a5f98-1493-41cb-927f-80ca04903b28",
        "data": [
          {
            "text": "histogram",
            "userDefined": False
          }
        ],
        "isTemplate": False,
        "count": 0,
        "updated": 0
      },
      {
        "id": "4ad919c3-4e82-45d1-86c0-fb57fdb5b4e6",
        "data": [
          {
            "text": "view histogram of ",
            "userDefined": False
          },
          {
            "text": "farmacia_nro_soe",
            "alias": "columns_select",
            "meta": "@columns_select",
            "userDefined": True
          }
        ],
        "isTemplate": False,
        "count": 0,
        "updated": 0
      },
      {
        "id": "3dfb950d-73cf-4ef0-80c6-a42542d24b5f",
        "data": [
          {
            "text": "Histogram of ",
            "userDefined": False
          },
          {
            "text": "farmacia_nro_soe",
            "alias": "columns_select",
            "meta": "@columns_select",
            "userDefined": True
          }
        ],
        "isTemplate": False,
        "count": 0,
        "updated": 0
      },
      {
        "id": "8132ab66-974a-4ccc-b3c9-212d307f1d8e",
        "data": [
          {
            "text": "I want see the histogram of ",
            "userDefined": False
          },
          {
            "text": "farmacia_nro_soe",
            "alias": "columns_select",
            "meta": "@columns_select",
            "userDefined": True
          }
        ],
        "isTemplate": False,
        "count": 0,
        "updated": 0
      }
    ]
        return usersays

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
