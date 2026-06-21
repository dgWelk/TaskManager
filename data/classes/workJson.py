import json

from data.saves.libraries.LibrarySettings import settings

class workJson:
    def __init__(self):
        self.adress = [
            'data/saves/settings.json',
            '../saves/settings.json'
        ]
        self.settings = settings

        with open(self.adress[0]) as json_file:
            self.data = json.load(json_file)

    def readJson(self, way=0):
        with open(self.adress[way], 'r', encoding='utf-8') as jsonfile:
            return json.load(jsonfile)

    def writeJson(self, way=0):
        with open(self.adress[way], 'w', encoding='utf-8') as jsonfile:
            json.dump(self.data, jsonfile, indent=4)

    def changeSettingsTime(self, adress, be='On', type=None):
        self.data['time'][adress]['be'] = be
        if type:
            self.data['time'][adress]['type'] = type
        self.writeJson()