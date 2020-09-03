from mapbox import Static


class MapBox():

    PATH = '../maps/'

    def __init__(self, points, id):
        self.points = points
        self.id = id

    @property
    def points(self):
        return self.__points

    @property
    def id(self):
        return self.__id

    @points.setter
    def points(self, points):
        self.__points = points

    @id.setter
    def id(self, id):
        self.__id = id

    def createMapBoxMap(self):
        service = Static()
        fullPathImage = self.PATH + self.id + '.png'
        features = [self.createFeature(point) for point in self.points]
        response = None
        if len(features) == 1:
            print(features[0]['geometry']['coordinates'][0])
            print(features[0]['geometry']['coordinates'][1])
            response = service.image('mapbox.satellite', lon=features[0]['geometry']['coordinates'][0], lat=features[0]['geometry']['coordinates'][1], z=15, features=features)
        else:
            response = service.image('mapbox.satellite', features=features)
        print(response)
        with open(fullPathImage, 'wb') as output:
            _ = output.write(response.content)

    def createFeature(self, coordinates):
        feature = {
            'type': 'Feature',
            'properties': {'name': 'Portland, OR'},
            'geometry': {
                'type': 'Point',
                'coordinates': [float(str("%.4f" % coordinates[1])), float(str("%.4f" % coordinates[0]))]}
        }
        return feature
