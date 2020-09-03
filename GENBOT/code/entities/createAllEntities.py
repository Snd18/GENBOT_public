from entities import EntityEntryFile as entryFile
from entities import EntityMainFile as entityFile
from entities import Entry as entry


def createAllEntities(db):
    '''
    Create all entities files: [fieldName].json and [fieldName]_entries_en.json.
    Each entity has two json files.
    '''
    # control id for entities
    id = 0
    # create owns entitys
    entrys_for_select = []
    for field in db.table.fields:
        en = entry.Entry(field.name, field.synonyms)
        entrys_for_select.append(en.entry)
        if 'sys.' not in field.entity_meta:
            e = entityFile.EntityMainFile(generateUIDfromId(id), field.name, False)
            e.writeToFile()
            entrys = []
            for value in field.values:
                en = entry.Entry(value, [value])
                entrys.append(en.entry)
            e = entryFile.EntityEntryFile(field.name, entrys)
            e.writeToFile()
            id = id + 1
    # create columns_select entity
    e = entityFile.EntityMainFile(generateUIDfromId(id), 'columns_select', True)
    e.writeToFile()
    e = entryFile.EntityEntryFile('columns_select', entrys_for_select)
    e.writeToFile()
    id = id + 1
    # create other entities for graphs
    # simple Graph
    types = ['pie', 'histogram', 'linesSerie', 'pointsSerie']
    entrys = []
    for item in types:
        en = entry.Entry(item, [item])
        entrys.append(en.entry)
    e = entryFile.EntityEntryFile('simple_graph', entrys)
    e.writeToFile()
    e = entityFile.EntityMainFile(generateUIDfromId(id), 'simple_graph', True)
    e.writeToFile()
    id = id + 1
    # complex Graph
    types = ['pointsVs', 'linesSerie', 'pointsSerie', 'linesVs']
    entrys = []
    for item in types:
        en = entry.Entry(item, [item])
        entrys.append(en.entry)
    e = entryFile.EntityEntryFile('complex_graph', entrys)
    e.writeToFile()
    e = entityFile.EntityMainFile(generateUIDfromId(id), 'complex_graph', True)
    e.writeToFile()

def generateUIDfromId(id):
    uid = "f4ee0fc1-9d18-46dd-8c8e-1da27dc57bb0"
    uid = uid[:-len(str(id))] + str(id)
    return uid
