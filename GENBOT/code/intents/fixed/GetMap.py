from utils import utils


class GetMap():

    filepath = "../outputs/v4/intents/"

    name = 'GetMap'

    @property
    def intent(self):
        intent = {
            "id": "66102232-ec5f-4343-84b6-f3bf270c22b9",
            "name": "GetMap",
            "auto": True,
            "contexts": [],
            "responses": [{
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [{
                    "id": "afa918a3-ca4f-41f3-92aa-74eabd1679ca",
                    "required": True,
                    "dataType": "@sys.number",
                    "name": "idImage",
                    "value": "$idImage",
                    "prompts": [{
                        "lang": "en",
                        "value": "Please, press the button again"
                    }],
                    "promptMessages": [],
                    "noMatchPromptMessages": [],
                    "noInputPromptMessages": [],
                    "outputDialogContexts": [],
                    "isList": False
                }],
                "messages": [{
                    "type": 0,
                    "lang": "en",
                    "condition": "",
                    "speech": []
                }],
                "defaultResponsePlatforms": {},
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
                "id": "8a6021f7-5746-4c33-a8fd-95044243f1fd",
                "data": [{
                    "text": "the map is:",
                    "userDefined": False
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "b6d3ae1d-6c04-4535-8b52-5c9ecbc92f30",
                "data": [
                    {
                        "text": "The map is: ",
                        "userDefined": False
                    },
                    {
                        "text": "74897864645",
                        "alias": "idImage",
                        "meta": "@sys.number",
                        "userDefined": False
                    }
                ],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            }
        ]
        return usersays

    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
        utils.writeToFile(self.usersays, self.filepath + self.name + '_usersays_en.json')
