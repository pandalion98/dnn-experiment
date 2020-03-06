import json
import os

filepaths = list()
dataDir = '/content/drive/Shared drives/Colpz Mirror/doaj-extracted/doaj_article_data_2020-02-25/'
filesInDir = os.listdir(dataDir);
for fileName in filesInDir:
    filepaths.append(os.path.join(dataDir, fileName))

titlePath = '/content/drive/Shared drives/Colpz Mirror/doaj_parsed/titles.txt'

for filePath in filepaths:
    data = json.load(open(filePath, mode='br'))

    for json_element in data:
        file = open(titlePath, "w")
        try:
            file.write(json_element['bibjson']['title'])
            file.close()  # This close() is important
        except:
            file.close()
            continue
