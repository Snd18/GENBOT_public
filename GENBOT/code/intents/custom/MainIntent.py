from utils import utils


class MainIntent():
    # [nameIntent].json content

    path = "../outputs/v4/intents/"

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def json(self):
        intent = {
            "id": str(self.id),
            "name": self.name,
            "auto": True,
            "contexts": [],
            "responses": [
                {
                    "resetContexts": False,
                    "affectedContexts": [],
                    "parameters": [],
                    "messages": [
                    {
                        "type": 0,
                        "lang": "en",
                        "speech": []
                    }
                    ],
                    "defaultResponsePlatforms": {},
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": True,
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": []
        }
        return intent

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    def writeToFile(self):
        utils.writeToFile(self.json, self.filepath + self.name + '.json')
