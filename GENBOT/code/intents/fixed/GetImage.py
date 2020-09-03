from utils import utils


class GetImage():

    filepath = "../outputs/v4/intents/"

    name = 'GetImage'

    @property
    def intent(self):
        intent = {
            "id": "d5499278-d91e-413d-8cd8-ea44ba556912",
            "name": "GetImage",
            "auto": True,
            "contexts": [],
            "responses": [{
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [{
                    "id": "bf3185de-73cb-4ba8-85e7-451b98543d7d",
                    "required": False,
                    "dataType": "@sys.number",
                    "name": "idImage",
                    "value": "$idImage",
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
        }
        return intent

    @property
    def usersays(self):
        usersays = [
            {
                "id": "d103e4b7-1866-4dc8-b11a-61798d3b96d0",
                "data": [
                    {
                        "text": "image ",
                        "userDefined": False
                    },
                    {
                        "text": "987568572545",
                        "alias": "idImage",
                        "meta": "@sys.number",
                        "userDefined": True
                    }
                ],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "addaea99-4890-4975-b111-6bb7407df116",
                "data": [
                    {
                        "text": "The image is ",
                        "userDefined": False
                    },
                    {
                        "text": "789545125262",
                        "alias": "idImage",
                        "meta": "@sys.number",
                        "userDefined": False
                    }
                ],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "8ea776b7-a354-4f5c-a4e7-676844c628ed",
                "data": [
                    {
                        "text": "The image id is ",
                        "userDefined": False
                    },
                    {
                        "text": "201589546523",
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
