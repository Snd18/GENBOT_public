from utils import utils


class GetTypeComplexGraph():

    filepath = "../outputs/v4/intents/"

    name = 'Complex graph - type'

    @property
    def intent(self):
        intent = {
     "id": "55fce9e4-5e9e-4437-ba56-f3c310f51cd7",
      "parentId": "7c308982-f0d2-4129-b5d4-5f01d21545b8",
      "rootParentId": "7c308982-f0d2-4129-b5d4-5f01d21545b8",
      "name": "Complex graph - type",
      "auto": True,
      "contexts": [
        "Twovargraph-followup"
      ],
      "responses": [
        {
          "resetContexts": False,
          "action": "Twovargraph.Twovargraph-custom",
          "affectedContexts": [],
          "parameters": [
            {
              "id": "0490c5d8-4b4c-4fe0-8dd4-a8a6841b5261",
              "required": False,
              "dataType": "@complex_graph",
              "name": "complex_graph",
              "value": "$complex_graph",
              "promptMessages": [],
              "noMatchPromptMessages": [],
              "noInputPromptMessages": [],
              "outputDialogContexts": [],
              "isList": False
            }
          ],
          "messages": [
            {
              "type": 0,
              "lang": "en",
              "condition": "",
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
    "id": "060e272d-2390-4ff6-be0e-00a7aeb5d1d5",
    "data": [
    {
    "text": "linesVs",
    "alias": "complex_graph",
    "meta": "@complex_graph",
    "userDefined": True
    }
    ],
    "isTemplate": False,
    "count": 0,
    "updated": 0
    },
    {
    "id": "1dd28e9c-05b7-4160-95af-5aa170786735",
    "data": [
    {
    "text": "the type is: ",
    "userDefined": False
    },
    {
    "text": "pointsVs",
    "alias": "complex_graph",
    "meta": "@complex_graph",
    "userDefined": False
    }
    ],
    "isTemplate": False,
    "count": 0,
    "updated": 0
    },
    {
    "id": "4c8901ad-29d4-4c3f-b6a1-d7679c343cbc",
    "data": [
    {
    "text": "type is ",
    "userDefined": False
    },
    {
    "text": "pointsSerie",
    "alias": "complex_graph",
    "meta": "@complex_graph",
    "userDefined": False
    }
    ],
    "isTemplate": False,
    "count": 1,
    "updated": 0
    },
    {
    "id": "c81dddd1-c732-4c88-9fd4-75b70d5a756f",
    "data": [
    {
    "text": "The type is : ",
    "userDefined": False
    },
    {
    "text": "linesVs",
    "alias": "complex_graph",
    "meta": "@complex_graph",
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
