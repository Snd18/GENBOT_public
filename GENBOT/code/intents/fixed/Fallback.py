from utils import utils


class Fallback():

    filepath = "../outputs/v4/intents/"

    name = 'Default Fallback Intent'

    @property
    def intent(self):
        intent = {
            "id": "3be18eea-c9d4-4adf-b83b-9a6e40da8d80",
            "name": "Default Fallback Intent",
            "auto": True,
            "contexts": [],
            "responses": [{
                "resetContexts": False,
                "action": "input.unknown",
                "affectedContexts": [],
                "parameters": [],
                "messages": [{
                    "type": 0,
                    "lang": "en",
                    "condition": "",
                    "speech": [
                        "I didn\u0027t get that. Can you say it again?",
                        "I missed what you said. What was that?",
                        "Sorry, could you say that again?",
                        "Sorry, can you say that again?",
                        "Can you say that again?",
                        "Sorry, I didn\u0027t get that. Can you rephrase?",
                        "Sorry, what was that?",
                        "One more time?",
                        "What was that?",
                        "Say that one more time?",
                        "I didn\u0027t get that. Can you repeat?",
                        "I missed that, say that again?"
                    ]
                }],
                "defaultResponsePlatforms": {},
                "speech": []
            }],
            "priority": 500000,
            "webhookUsed": False,
            "webhookForSlotFilling": False,
            "fallbackIntent": True,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
        return intent

    def writeToFile(self):
        utils.writeToFile(self.intent, self.filepath + self.name + '.json')
