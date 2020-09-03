from utils import utils


class Welcome():

    filepath = "../outputs/v4/intents/"

    name = 'Default Welcome Intent'

    def __init__(self, database):
        self.database = database

    @property
    def intent(self):
        intent = {
            "id": "f91b1c18-bb10-42d5-9e3d-2441ceac0bae",
            "name": "Default Welcome Intent",
            "auto": True,
            "contexts": [],
            "responses": [{
                "resetContexts": False,
                "action": "input.welcome",
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
                          "text": self.getWelcomeText(),
                          "parse_mode": "html"
                        }
                      }
                  }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }],
            "priority": 500000,
            "webhookUsed": False,
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [{
                "name": "WELCOME"
            }],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
        return intent

    @property
    def usersays(self):
        usersays = [
            {
                "id": "9a03a47d-3610-4abd-9b21-6052b6b76c77",
                "data": [{
                    "text": "just going to say hi",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "9391e254-e8c7-4325-9dfe-85f627c978ed",
                "data": [{
                    "text": "heya",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "1e2a1cbb-9344-4673-8ce2-ddc58e1eed22",
                "data": [{
                    "text": "hello hi",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "857de086-1bae-43c2-bdc4-923d952f3efc",
                "data": [{
                    "text": "howdy",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "e81bf13b-b8a2-4a64-ace0-40efbdd971cc",
                "data": [{
                    "text": "hey there",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "864e68a8-8df8-4226-95ab-c0f5c1d4a322",
                "data": [{
                    "text": "hi there",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 1,
                "updated": 0
            },
            {
                "id": "442895ef-1734-49bc-a9a8-f7813c117d09",
                "data": [{
                    "text": "greetings",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "3b2c0c6b-6eae-471e-a665-d65f56a951ca",
                "data": [{
                    "text": "hey",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "a170435b-cc40-4889-8364-3a7492265327",
                "data": [{
                    "text": "long time no see",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "965adf76-9c40-4a38-8999-cd7dd5e32da1",
                "data": [{
                    "text": "hello",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "f4ee0fc1-9d18-46dd-8c8e-1da27dc57bb4",
                "data": [{
                    "text": "lovely day isn\u0027t it",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "de38c0d2-87a0-4f26-84f7-71e497adbb96",
                "data": [{
                    "text": "I greet you",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "6893879f-c27f-4a28-840c-af5851b3e716",
                "data": [{
                    "text": "hello again",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "70da9eba-ee66-4bb5-8e17-078927f44093",
                "data": [{
                    "text": "hi",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "16205a9f-6b3a-437b-a2af-a8e2793856a4",
                "data": [{
                    "text": "hello there",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "b238c71b-bb4b-48db-9fd5-fc89aec18845",
                "data": [{
                    "text": "a good day",
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

    def getWelcomeText(self):
        return "Hi human!\n\nI'm a chatbot created to help to translate natural language to SQL. I'll give you data and other visual information from the database I am connect to.\n\nIf you still don't know what to do or say please ask for help."

    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
        utils.writeToFile(self.usersays, self.filepath + self.name + '_usersays_en.json')
