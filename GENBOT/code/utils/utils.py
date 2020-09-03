from urllib.request import urlopen
import pandas as pd
import json
import os


def getDF(table):
    '''
    Returns a df from csv given its url
    '''
    f = None
    r = None
    try:
        # download csv
        r = urlopen(table.csv_url)
        # write to a local file
        filename = table.csv_local
        f = open(filename, "wb")
        f.write(r.read())
        r.close()
        f.close()
        # read csv with pandas
        df = pd.read_csv(filename, header=table.headers, delimiter=table.delimiter, encoding='latin1', nrows=20)
        return df
    except Exception as e:
        print(e)
        raise
    finally:
        if r:
            r.close()
        if f:
            f.close()


#def saveToCSV(df, path):
#    df.to_csv(path)

def removeCSV(filename):
    if os.path.exists(filename):
        os.remove(filename)

def createAgent(id):
    zipFolder(id, "../outputs/v4")
    moveFile("../outputs/v4/" + id + '.zip', '../agents/')

def zipFolder(filename, dirFolder):
    if os.path.exists(dirFolder):
        os.system('cd ' + dirFolder + '&& zip -r ' + filename + ' .')

def moveFile(inDir, outDir):
    if os.path.exists(inDir):
        os.system('mv ' + inDir + ' ' + outDir)


def writeToFile(data, filename):
    '''
    Write json to a file
    '''
    '''
    with io.open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=True)

    '''
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def clearDirs():
    dir1 = "../outputs/v4/entities/*"
    dir2 = "../outputs/v4/intents/*"
    os.system('rm ' + dir1 + '&& rm ' + dir2)


def clearData(string, charToPut):
    '''
    Clear data from invalid character.
    Invalid characters will be changed by specified character.
    '''
    allowedChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','_','1','2','3','4','5','6','7','8','9','0']
    string = list(string)
    for i in range(0, len(string)):
        if not string[i] in allowedChar:
            string[i] = charToPut
    string = ''.join(string)
    return string
