from data.classes.workCSV import workCSV
from data.scripts.workTime import giveTime

operator = workCSV()

data = [
    {'Date': giveTime(), 'Task':'Любить вечно'}
]
print(operator.readCSV())
#print(operator.writeCSV(data))
