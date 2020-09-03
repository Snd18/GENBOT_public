import folium


class Folium():

    PATH = '../maps/'

    def __init__(self, points, id, extrainfo):
        self.points = points
        self.id = id
        self.extrainfo = extrainfo

    @property
    def points(self):
        return self.__points

    @property
    def id(self):
        return self.__id

    @property
    def extrainfo(self):
        return self.__extrainfo

    @points.setter
    def points(self, points):
        self.__points = points

    @id.setter
    def id(self, id):
        self.__id = id

    @extrainfo.setter
    def extrainfo(self, extrainfo):
        self.__extrainfo = extrainfo

    def createFoliumMap(self):
        fullPathImage = self.PATH + self.id + 'FoliumMap.html'
        m = folium.Map(location=[self.points[0][0], self.points[0][1]], zoom_start=13)
        if self.extrainfo != []:
            info = self.preparateExtrainfo()
            tooltip = 'Click me!'
            for i, point in enumerate(self.points):
                popup = folium.Popup(info[i], max_width=300)
                folium.Marker([point[0], point[1]], popup=popup, tooltip=tooltip).add_to(m)
        m.save(fullPathImage)

    def preparateExtrainfo(self):
        result = []
        for item in self.extrainfo:
            aux = ''
            for key in item:
                aux = aux + '<p><b>' + key + '</b>: ' + str(item[key]) + '</p>'
            result.append(aux)
        return result
