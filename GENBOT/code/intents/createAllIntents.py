from intents.fixed import GetFile as gfile
from intents.fixed import GetImage as gimage
from intents.fixed import GetMap as gmap
from intents.fixed import GetTypeComplexGraph as gtcomplex
from intents.fixed import GetTypeSimpleGraph as gtsimple
from intents.fixed import Help as help
from intents.fixed import AskMap as amap
from intents.fixed import AskComplexGraph as acomplex
from intents.fixed import AskSimpleGraph as asimple
from intents.fixed import Fallback as fallback
from intents.fixed import Welcome as welcome


def createAllIntents(data):
    i = gfile.GetFile()
    i.writeToFile()

    h = gimage.GetImage()
    h.writeToFile()

    a = gtcomplex.GetTypeComplexGraph()
    a.writeToFile()

    b = gtsimple.GetTypeSimpleGraph()
    b.writeToFile()

    c = help.Help(data.db, data.properties)
    c.writeToFile()

    if data.properties:
        if data.properties.info_map:
            e = amap.AskMap(data.db.name, data.db.table.name, data.properties.info_map.filter_field, data.properties.info_map.coorY_field, data.properties.info_map.coorX_field, data.properties.info_map.extra_info_fields )
            e.writeToFile()
            d = gmap.GetMap()
            d.writeToFile()

    f = acomplex.AskComplexGraph(data.db.name, data.db.table.name)
    f.writeToFile()

    g = asimple.AskSimpleGraph(data.db.name, data.db.table.name)
    g.writeToFile()

    j = fallback.Fallback()
    j.writeToFile()

    k = welcome.Welcome(data.db)
    k.writeToFile()
