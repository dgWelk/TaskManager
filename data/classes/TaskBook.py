from data.scripts.workTime import giveTime
from data.scripts.bridgeCSVBOOK import constructor

class TaskBook:
    def __init__(self, data_import):
        self.fieldnames = ['Date', 'Task']
        self.data = data_import if data_import else []
        self.menu = f'''----- Menu -----
1. Add Task
2. Delete Task
3. Show Tasks
4. Exit
----------------'''

    def addTask(self, task):
        self.data.append(constructor(giveTime(), task))

    def delTask(self, num):
        adress =  int(num) - 1
        del self.data[adress]

    def showTasks(self):
        print(f'----------------')

        if len(self.data) == 0:
            print('U dont have tasks')
        else:
            print('U have this tasks:')
            for ind, task in enumerate(self.data):
                print(f'{ind+1}. {task['Task']} (Created: {task['Date']})')

        print('----------------')

    def dropData(self):
        return self.data

    def importData(self, data_import):
        self.data = data_import

