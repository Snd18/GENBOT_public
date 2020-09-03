import time
import os


class Plantuml():

    txtPath = "./plantuml/schema.txt"
    imagesPath = '../images/'

    def __init__(self, model):
        self.model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def getPlantumlImage(self):
        self.createUMLStringModel()
        id = self.createPlantumlImage()
        return id

    def getId(self):
        id = time.strftime("%Y%m%d%H%M%S")
        return id

    def createPlantumlImage(self):
        cmd = 'java -jar ./plantuml/plantuml.jar ' + self.txtPath
        os.system(cmd)
        idImage = self.getId()
        cmd = 'cp ./plantuml/schema.png ' + self.imagesPath + idImage + '.png'
        os.system(cmd)
        return idImage

    def createUMLStringModel(self):
        stringModel = self.getUMLStringModel()
        file = open(self.txtPath, "w")
        file.write(stringModel)
        file.close()

    def getUMLStringModel(self):
        text = '@startuml\n'
        text = text + 'class "' + self.model.db.name + ':DB"{\n}\n'
        text = text + 'class "' + self.model.db.table.name + ':Table"{\n'
        text = text + 'csv : string = "' + self.model.db.table.csv_url[:10] + '...' + '"\n'
        text = text + '}\n'
        text = text + '"' + self.model.db.name + ':DB" *-- "' + self.model.db.table.name + ':Table"\n'
        for field in self.model.db.table.fields:
            text = text + 'class "' + field.name + ':Field"{\n'
            text = text + 'DBtype : string = "' + field.db_meta + '"\n'
            text = text + 'DFtype : string = "' + field.entity_meta + '"\n'
            text = text + '}\n'
            text = text + '"' + self.model.db.table.name + ':Table" *-- "' + field.name + ':Field"\n'
        text = text + '@enduml'
        return text
