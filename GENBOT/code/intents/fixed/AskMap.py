from utils import utils


class AskMap():

    filepath = "../outputs/v4/intents/"

    name = 'Ask for map'

    def __init__(self, dbname, tablename, field, lat, lon, extraInfo):
        self.dbname = dbname
        self.tablename = tablename
        self.field = field
        self.lat = lat
        self.lon = lon
        self.extraInfo = extraInfo

    @property
    def intent(self):
        intent = {
            "id":"67ad8674-a0cc-4954-9efd-8f3da9890440",
            "name":"Ask for map",
            "auto":True,
            "contexts":[

            ],
            "responses":[
                {
                    "resetContexts":False,
                    "affectedContexts":[

                    ],
                    "parameters":[
                        {
                            "id":"80628baa-e046-4687-9e19-2ee972502795",
                            "required":False,
                            "dataType":"",
                            "name":"tablename",
                            "value":self.tablename,
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
                            "id":"2e6466a2-e4bd-448f-bb03-fe51bddca645",
                            "required":False,
                            "dataType":"",
                            "name":"fieldname",
                            "value":self.field.name,
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
                            "id":"4e23e114-c32c-4785-ad80-dec725ab9f88",
                            "required":False,
                            "dataType":"",
                            "name":"databasename",
                            "value":self.dbname,
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
                            "id":"3ccc9c00-aefe-4e26-9a93-d16fa9715b29",
                            "required":False,
                            "dataType":"",
                            "name":"latitude",
                            "value":self.lat,
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
                            "id":"becba47e-814c-4a89-836b-391f4c7ffa4e",
                            "required":False,
                            "dataType":"",
                            "name":"longitude",
                            "value":self.lon,
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
                            "id":"54fd6fdb-e905-4f7f-9003-a1536d94bb54",
                            "required":False,
                            "dataType":"",
                            "name":"extraInfo",
                            "value": self.extraInfo,
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
                            "id":"54fd6fdb-e905-4f7f-9003-a1536d94bb53",
                            "required": True,
                            "dataType": self.field.entity_meta,
                            "name":"valueMap",
                            "value": "$valueMap",
                            "promptMessages":[

                            ],
                            "noMatchPromptMessages":[

                            ],
                            "noInputPromptMessages":[

                            ],
                            "outputDialogContexts":[

                            ],
                            "isList":True
                        }
                    ],
                    "messages":[
                        {
                            "type":0,
                            "lang":"en",
                            "condition":"",
                            "speech":[

                            ]
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
        "id":"5644eb73-3cd1-4794-8b1a-eec7bffa8d67",
        "data":[
        {
        "text":"Where is ",
        "userDefined":False
        },
        {
        "text":"this",
        "alias":"valueMap",
        "meta":self.field.entity_meta,
        "userDefined":True
        },
        {
        "text":"?",
        "userDefined":False
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"be6f7003-b129-4eef-8566-f2d9584e0605",
        "data":[
        {
        "text":"I want a  map of ",
        "userDefined":False
        },
        {
        "text":"this",
        "alias":"valueMap",
        "meta":self.field.entity_meta,
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"dc7a6235-a3e3-41cc-b9e5-d6dd6f1b782a",
        "data":[
        {
        "text":"I want to know where is ",
        "userDefined":False
        },
        {
        "text":"this",
        "alias":"valueMap",
        "meta":self.field.entity_meta,
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"a594d40d-598d-4107-85f5-84977bcb8875",
        "data":[
        {
        "text":"display on map ",
        "userDefined":False
        },
        {
        "text":"this",
        "alias":"valueMap",
        "meta":self.field.entity_meta,
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"36854365-bace-4b22-be1d-132c528da6e1",
        "data":[
        {
        "text":"display ",
        "userDefined":False
        },
        {
        "text":"Maria de los amores",
        "alias":"valueMap",
        "meta":self.field.entity_meta,
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        },
        {
        "id":"9aab4ae9-ba51-40ca-a420-29b5a2d87df9",
        "data":[
        {
        "text":"show me on map ",
        "userDefined":False
        },
        {
        "text":"pavones",
        "alias":"valueMap",
        "meta":self.field.entity_meta,
        "userDefined":True
        }
        ],
        "isTemplate":False,
        "count":0,
        "updated":0
        }
        ]
        return usersays

    @property
    def dbname(self):
        return self.__dbname

    @property
    def tablename(self):
        return self.__tablename

    @property
    def field(self):
        return self.__field

    @dbname.setter
    def dbname(self, dbname):
        self.__dbname = dbname

    @tablename.setter
    def tablename(self, tablename):
        self.__tablename = tablename

    @field.setter
    def field(self, field):
        self.__field = field

    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
        utils.writeToFile(self.usersays, self.filepath + self.name + '_usersays_en.json')
