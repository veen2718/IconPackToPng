from os import path,listdir,rename,chdir
from zipfile import ZipFile
import json
import xml.etree.ElementTree as ET
from vars import iconDir, pngDir, appfilterDir

baseDir = path.abspath(path.dirname(__file__))

def setup():
    chdir(iconDir)
    iconPacksApks = [pack for pack in listdir() if '.apk' in pack]
    
    for pack in iconPacksApks:
        rename(pack, pack.replace('.apk','.zip'))
    iconPackZips = [pack for pack in listdir() if '.zip' in pack]
    for pack in iconPackZips:
        with ZipFile(pack,'r') as zipRef:
            zipRef.extractall(pack.replace('.zip','Ref'))
    chdir(baseDir)

def get():
    chdir(iconDir)

    iconPacks = [pack for pack in listdir() if '.zip' not in pack and '.apk' not in pack]
    packs = []
    for pack in iconPacks:
        tree = ET.parse(path.join(pack,appfilterDir))
        root = tree.getroot()
        packData = {}
        for child in root:
            component = child.attrib['component']
            component = component.replace("ComponentInfo{","").replace("}","")
            component = component.split("/")[0]
            packData[component] = child.attrib['drawable']
        print(json.dumps(packData,indent=4))
    return packs


get()