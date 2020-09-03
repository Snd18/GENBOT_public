from flask import jsonify


class Response():

    MAPTYPE = 'MAP'
    IMAGETYPE = 'IMAGE'
    ONEVARGRAPHTYPE = 'ONEVARGRAHP'
    TWOVARGRAPHTYPE = 'TWOVARGRAHP'
    SIMPLETYPE = 'SIMPLE'

    # types of one var graph
    #TYPESSIMPLEGRAPH = ['pie', 'histogram', 'linesSerie', 'pointsSerie']
    # types of two var graph
    #TYPESCOMPLEXGRAPH = ['pointsVs', 'linesVs', 'pointsSeries', 'linesSerie']

    TYPES_SIMPLEGRAPH = ['pie', 'histogram', 'line graph', 'scatter plot']
    TYPES_COMPLEXGRAPH = ['scatter plot (X vs Y)', 'line graph (X vs Y)', 'scatter plot (series)', 'line graph (series)']



    simpleGraphButtons = [[{'text': type, 'callback_data': 'the type is: ' + type}] for type in TYPES_SIMPLEGRAPH]
    complexGraphButtons = [[{'text': type, 'callback_data': 'the type is: ' + type}] for type in TYPES_COMPLEXGRAPH]

    imageText = 'Please, wait a moment and then press the button below to get the graph you ask for.'
    mapText = 'Please, wait a moment and then press the button below to get the map you ask for.'
    simpleGraphText = 'What kind of graph do you want?'
    simpleText = 'Can you repeat it?'
    complexGraphText = simpleGraphText

    def __init__(self, id, text):
        self.id = id
        self.simple = jsonify({'fulfillmentText': text})
        self.complexGraph = jsonify({
            "fulfillmentMessages": [{
                "payload": {
                    "telegram": {
                        "text": self.complexGraphText,
                        "reply_markup": {
                            "inline_keyboard": self.complexGraphButtons
                        }
                    }
                },
                "platform": "TELEGRAM"
            }]
        })
        self.simpleGraph = jsonify({
            "fulfillmentMessages": [{
                "payload": {
                    "telegram": {
                        "text": self.simpleGraphText,
                        "reply_markup": {
                            "inline_keyboard": self.simpleGraphButtons
                        }
                    }
                },
                "platform": "TELEGRAM"
            }]
        })
        self.image = jsonify({
            "fulfillmentMessages": [{
                "payload": {
                    "telegram": {
                        "text": self.imageText,
                        "reply_markup": {
                            "inline_keyboard": [[{'text': 'Show graph', 'callback_data': 'the image is: ' + str(self.id)}]]
                        }
                    }
                },
                "platform": "TELEGRAM"
            }]
        })
        self.map = jsonify({
            "fulfillmentMessages": [{
                "payload": {
                    "telegram": {
                        "text": self.mapText,
                        "reply_markup": {
                            "inline_keyboard": [[{'text': 'Show map', 'callback_data': 'the map is: ' + str(self.id)}]]
                        }
                    }
                },
                "platform": "TELEGRAM"
            }]
        })

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    '''
    def getResponse(self, type):

        if type == self.MAPTYPE:
            mapButton = [[{'text': 'Show map', 'callback_data': 'the map is: ' + self.id}]]
            res = self.mapRes
            res['fulfillmentMessages'][0]['payload']['telegram']['reply_markup']['inline_keyboard'] = mapButton
        elif type == self.IMAGETYPE:
            imageButton = [[{'text': 'Show graph', 'callback_data': 'the image is: ' + self.id}]]
            res = self.imageRes
            res['fulfillmentMessages'][0]['payload']['telegram']['reply_markup']['inline_keyboard'] = imageButton
        elif type == self.ONEVARGRAPHTYPE:
            res = self.oneVarGraphRes
        elif type == self.TWOVARGRAPHTYPE:
            res = self.twoVarGraphRes
        elif type == self.SIMPLETYPE:
            res = self.simpleRes
        #elif type == self.GETIMAGETYPE:
        return jsonify(res)
    '''
