
class Response():

    def __init__(self, text, image, buttons, inline, context):
        self.text = text
        self.image = image
        self.buttons = buttons
        self.context = context
        self.inline = inline
        self.response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "telegram": {
                            "text": self.text
                            ,
                            "reply_markup": {
                                "keyboard": self.buttons,
                                "one_time_keyboard": True,
                                "resize_keyboard": True,
                                "inline_keyboard": self.inline
                            }
                        }
                    },
                    "platform": "TELEGRAM"
                },
                {
                    "image": {
                        "imageUri": self.image
                    },
                    "platform": "TELEGRAM"
                }
            ],
            "outputContexts": self.context
        }

    @property
    def text(self):
        return self.__text

    @property
    def imageUri(self):
        return self.__imageUri

    @property
    def buttons(self):
        return self.__buttons

    @property
    def context(self):
        return self.__context

    @text.setter
    def text(self, text):
        self.__text = text

    @imageUri.setter
    def imageUri(self, imageUri):
        self.__imageUri = imageUri

    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons

    @context.setter
    def context(self, context):
        self.__context = context
