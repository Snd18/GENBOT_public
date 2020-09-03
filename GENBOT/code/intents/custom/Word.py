

class Word():

    def __init__(self, text, alias, meta):
        self.text = text
        self.alias = alias
        self.meta = meta

    @property
    def text(self):
        return self.__text

    @property
    def alias(self):
        return self.__alias

    @property
    def meta(self):
        return self.__meta

    @property
    def word(self):
        word = None
        if self.alias and self.meta:
            # to represent entity text in training phrases
            word = {
                "text": self.text,
                "alias": self.alias,
                "meta": self.meta,
                "userDefined": False
            }
        else:
            # to represent plain text in training phrases
            word = {
                "text": self.text,
                "userDefined": False
            }
        return word

    @text.setter
    def text(self, text):
        self.__text = text

    @alias.setter
    def alias(self, alias):
        self.__alias = alias

    @meta.setter
    def meta(self, meta):
        self.__meta = meta
