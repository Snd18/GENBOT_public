from utils import utils


class GetTypeSimpleGraph():

    filepath = "../outputs/v4/intents/"

    name = 'Simple graph - type'

    @property
    def intent(self):
        intent = {
            "id": "dcb63e07-f3e1-4106-b8e7-94e55add2a83",
            "parentId": "e11b8917-20e9-4a82-b922-2736f8cdfc09",
            "rootParentId": "e11b8917-20e9-4a82-b922-2736f8cdfc09",
            "name": "Simple graph - type",
            "auto": True,
            "contexts": [
                "Onevargraph-followup"
            ],
            "responses": [{
                "resetContexts": False,
                "action": "Onevargraph.Onevargraph-custom",
                "affectedContexts": [],
                "parameters": [{
                    "id": "8c803291-3416-4877-9a9c-348d04162abf",
                    "required": True,
                    "dataType": "@simple_graph",
                    "name": "simple_graph",
                    "value": "$simple_graph",
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
                "id": "b6838af1-eccd-4ab9-b20e-ac38c83f132a",
                "data": [
                    {
                        "text": "The type is : ",
                        "userDefined": False
                    },
                    {
                        "text": "pie",
                        "alias": "simple_graph",
                        "meta": "@simple_graph",
                        "userDefined": False
                    }
                ],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            },
            {
                "id": "b008890f-2139-466a-8e2f-26ab80df8e62",
                "data": [{
                    "text": "histogram",
                    "alias": "simple_graph",
                    "meta": "@simple_graph",
                    "userDefined": True
                }],
                "isTemplate": False,
                "count": 0,
                "updated": 0
            }
        ]
        return usersays


    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
        utils.writeToFile(self.usersays, self.filepath + self.name + '_usersays_en.json')
