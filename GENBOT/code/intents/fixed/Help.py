from utils import utils


class Help():

    filepath = "../outputs/v4/intents/"

    name = 'Help'

    def __init__(self, database, properties):
        self.database = database
        self.properties = properties

    @property
    def intent(self):
        intent = {
            "id": "d8d27a26-c23d-4ad5-8293-67acaf15e1fe",
            "name": "Help",
            "auto": True,
            "contexts": [],
            "responses": [{
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [],
                "messages": [
                {
                  "type": 4,
                  "platform": "telegram",
                  "lang": "en",
                  "condition": "",
                  "payload": {
                    "telegram": {
                      "text": self.getHelpText(),
                      "parse_mode": "html"
                    }
                  }
                }
                ],
                "defaultResponsePlatforms": {"telegram": True},
                "speech": []
            }],
            "priority": 500000,
            "webhookUsed": True,
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
        return intent

    @property
    def usersays(self):
        usersays = [
            {
                "id": "1",
                "data": [{
                    "text": "help",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "2",
                "data": [{
                    "text": "i need help",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "3",
                "data": [{
                    "text": "i don't know what to do",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "4",
                "data": [{
                    "text": "please, help",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            }
        ]
        return usersays

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, database):
        self.__database = database

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties):
        self.__properties = properties

    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
        utils.writeToFile(self.usersays, self.filepath + self.name + '_usersays_en.json')

    def getHelpText(self):
        text = "You asked for help!\n\nYou can get data from \u003ci\u003e\u0027nametable\u0027\u003c/i\u003e table.\n\u003ci\u003e\u0027nametable\u0027\u003c/i\u003e have the following fields:\n\n"
        text.replace('nametable', self.database.table.name)
        for field in self.database.table.fields:
            sentence = "- \u003cb\u003e\u0027" + field.name + "\u0027\u003c/b\u003e \u003ci\u003e(" + field.db_meta + ")\u003c/i\u003e: " + str(field.values[0]) + ", " + str(field.values[1]) + ", " + str(field.values[2]) + ".\n"
            text = text + sentence
        text = text + "\nAlso you can ask for graphs with one or two variables.\nExample: \u0027A graph with " + self.database.table.fields[0].name + " and " + self.database.table.fields[1].name + "\u0027 or \u0027A graph for " + self.database.table.fields[0].name + "\u0027.\n\n"
        if self.properties:
            if self.properties.info_map:
                text = text + "...or maps if they are supported.\nExample: \u0027A map for \u003ciaddress\u003e\u0027."
                text.replace('adress', self.properties.info_map.filter_field.values[0])

        text.replace('nametable', self.database.table.name)

        return text
