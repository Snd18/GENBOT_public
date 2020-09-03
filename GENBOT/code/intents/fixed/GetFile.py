from utils import utils


class GetFile():

    filepath = "../outputs/v4/intents/"

    name = 'GetFile'

    @property
    def intent(self):
        intent = {
            "id": "d0eafb6e-8e0c-4cbd-a465-eb524818e991",
            "name": "GetFile",
            "auto": True,
            "contexts": [],
            "responses": [{
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [{
                    "id": "aff5c0fb-a924-404d-a024-a2014bb2ec0e",
                    "required": False,
                    "dataType": "@sys.number",
                    "name": "idFile",
                    "value": "$idFile",
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
                "id": "03d457b8-dea8-4524-b509-2a5737331a39",
                "data": [
                    {
                        "text": "file ",
                        "userDefined": False
                    },
                    {
                        "text": "201956284545",
                        "alias": "idFile",
                        "meta": "@sys.number",
                        "userDefined": False
                    }
                ],
                "isTemplate": False,
                "count": 1,
                "updated": 0
            },
            {
                "id": "2d534d5c-9bbb-4df6-ad5e-64b41e0f5bcc",
                "data": [
                    {
                        "text": "The file is ",
                        "userDefined": False
                    },
                    {
                        "text": "201933052244",
                        "alias": "idFile",
                        "meta": "@sys.number",
                        "userDefined": False
                    }
                ],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "37339c03-3c64-46ed-af5d-46726fcc0fdc",
                "data": [
                    {
                        "text": "The file number is: ",
                        "userDefined": False
                    },
                    {
                        "text": "20191105",
                        "alias": "idFile",
                        "meta": "@sys.number",
                        "userDefined": True
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
