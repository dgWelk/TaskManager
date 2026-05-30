import csv
from data.scripts.bridgeCSVBOOK import constructor

class workCSV:
    def __init__(self):
        self.adress = 'data/saves/tasks.csv'

    def readCSV(self):
        data = []

        with open(self.adress, 'r', encoding='utf-8') as csvfile:
            for row in csv.DictReader(csvfile):
                data.append(constructor(row['Date'], row['Task']))
        return data


    def writeCSV(self, data):
        with open(self.adress, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Task']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

