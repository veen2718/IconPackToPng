from os import path,listdir,rename
import json


iconDir = 'iconPacks'
pngDir = "\\res\drawable-nodpi-v4"


iconPacksApks = [pack for pack in listdir('iconPacks') if '.apk' in pack]

for pack in iconPacksApks:
    rename(pack, pack.replace('.apk','.zip'))