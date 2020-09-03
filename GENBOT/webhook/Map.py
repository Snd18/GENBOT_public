import db
import Folium as folium
import MapBox as mapbox
import math


class Map():

    PATH = '../maps/'
    SERVERIMG = 'https://9328b04b8186.ngrok.io/map?id='

    def __init__(self, filter, table, database, id, longitud, latitud, extrainfo):
        self.filter = filter
        self.table = table
        self.database = database
        self.id = id
        self.longitud = longitud
        self.latitud = latitud
        self.extrainfo = extrainfo

    @property
    def filter(self):
        return self.__filter

    @property
    def table(self):
        return self.__table

    @property
    def database(self):
        return self.__database

    @property
    def id(self):
        return self.__id

    @property
    def longitud(self):
        return self.__longitud

    @property
    def latitud(self):
        return self.__latitud

    @property
    def extrainfo(self):
        return self.__extrainfo

    @filter.setter
    def filter(self, filter):
        self.__filter = filter

    @table.setter
    def table(self, table):
        self.__table = table

    @database.setter
    def database(self, database):
        self.__database = database

    @id.setter
    def id(self, id):
        self.__id = id

    @longitud.setter
    def longitud(self, longitud):
        self.__longitud = longitud

    @latitud.setter
    def latitud(self, latitud):
        self.__latitud = latitud

    @extrainfo.setter
    def extrainfo(self, extrainfo):
        self.__extrainfo = extrainfo

    def utmToLatLng(self, zone, easting, northing, northernHemisphere=True):
        if not northernHemisphere:
            northing = 10000000 - northing

        a = 6378137
        e = 0.081819191
        e1sq = 0.006739497
        k0 = 0.9996

        arc = northing / k0
        mu = arc / (a * (1 - math.pow(e, 2) / 4.0 - 3 * math.pow(e, 4) / 64.0 - 5 * math.pow(e, 6) / 256.0))

        ei = (1 - math.pow((1 - e * e), (1 / 2.0))) / (1 + math.pow((1 - e * e), (1 / 2.0)))

        ca = 3 * ei / 2 - 27 * math.pow(ei, 3) / 32.0

        cb = 21 * math.pow(ei, 2) / 16 - 55 * math.pow(ei, 4) / 32
        cc = 151 * math.pow(ei, 3) / 96
        cd = 1097 * math.pow(ei, 4) / 512
        phi1 = mu + ca * math.sin(2 * mu) + cb * math.sin(4 * mu) + cc * math.sin(6 * mu) + cd * math.sin(8 * mu)

        n0 = a / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (1 / 2.0))

        r0 = a * (1 - e * e) / math.pow((1 - math.pow((e * math.sin(phi1)), 2)), (3 / 2.0))
        fact1 = n0 * math.tan(phi1) / r0

        _a1 = 500000 - easting
        dd0 = _a1 / (n0 * k0)
        fact2 = dd0 * dd0 / 2

        t0 = math.pow(math.tan(phi1), 2)
        Q0 = e1sq * math.pow(math.cos(phi1), 2)
        fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 - 9 * e1sq) * math.pow(dd0, 4) / 24

        fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 * e1sq - 3 * Q0 * Q0) * math.pow(dd0, 6) / 720

        lof1 = _a1 / (n0 * k0)
        lof2 = (1 + 2 * t0 + Q0) * math.pow(dd0, 3) / 6.0
        lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * math.pow(Q0, 2) + 8 * e1sq + 24 * math.pow(t0, 2)) * math.pow(dd0, 5) / 120
        _a2 = (lof1 - lof2 + lof3) / math.cos(phi1)
        _a3 = _a2 * 180 / math.pi

        latitude = 180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / math.pi

        if not northernHemisphere:
            latitude = -latitude

        longitude = ((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3

        return [latitude, longitude]


    def getMap(self):
        query = self.getMapQuery()
        try:
            # conectar con la bd
            con = db.DB("localhost", "root", "", self.database, 3306)
            # get result from db
            result = con.executeQuery(query)
            lonAndLat = []
            infoMap = []
            for row in result:
                lonAndLat.append(self.utmToLatLng(30,row[0], row[1]))
                if len(row) > 2:
                    mapElement = dict()
                    for i in range(2, len(row)):
                        mapElement[self.extrainfo.split(',')[i - 2]] = row[i]
                    infoMap.append(mapElement)
            mb = mapbox.MapBox(lonAndLat, self.id)
            mb.createMapBoxMap()
            f = folium.Folium(lonAndLat, self.id, infoMap)
            f.createFoliumMap()


        except Exception as e:
            print(e)
            raise e

        finally:
            # si la conexion se ha creado --> cerrarla
            if (con):
                con.close()

    def getMapQuery(self):
        # create string that contains fields for select statment
        fieldsToSelect = self.longitud + ', ' + self.latitud + ', '
        for item in self.extrainfo.split(','):
            fieldsToSelect = fieldsToSelect + item + ', '
        fieldsToSelect = fieldsToSelect[:-2]

        # create string that contains fields for where statment
        fieldsToWhere = ''
        for key in self.filter:
            fieldsToWhere = fieldsToWhere + key + " = '" + self.filter[key] + "' , "
        fieldsToWhere = fieldsToWhere[:-2]

        # create string to inster into group by statemt
        groupby = '1,2'
        for i, item in enumerate(self.extrainfo.split(',')):
            groupby = groupby + ',' + str(i + 3)

        query = "select fieldsToSelect from table where fieldsToWhere group by groupby"
        query = query.replace('table', self.table)
        query = query.replace('fieldsToSelect', fieldsToSelect)
        query = query.replace('fieldsToWhere', fieldsToWhere)
        query = query.replace('groupby', groupby)
        print(query)
        return query
