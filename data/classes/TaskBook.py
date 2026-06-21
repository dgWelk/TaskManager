from data.scripts.bridgeCSVBOOK import constructor
from data.classes.FormatDate import formatDate

operatorTime = formatDate()

class TaskBook:
    def __init__(self, data_import, settings):
        self.data = data_import if data_import else []
        self.settings = settings


        self.version = 'b.0.5'

        self.helmet = f'''----------------
Task Manager {self.version}'''

#-----------------------------------------------------------------------------------------------------------------------
        self.mainMenu = f'''{self.helmet}
----- Menu -----
1. Add Task
2. Change Task
3. Delete Task
4. Show Tasks
5. Save Tasks
----------------
6. Settings
----------------
0. Exit
----------------'''

        self.settingsMenu = f'''{self.helmet}
--- Settings ---
1. Change time format
----------------
9. Go back
----------------
0. Exit
----------------'''

        self.settingsTimeMenu = f'''{self.helmet}
- Settings Time -
1. Change day format
2. Change month format
3. Change year format
4. Change hour format
5. Change minute format
6. Change seconds format
----------------
9. Go back
----------------
0. Exit
----------------'''

    def addTask(self, task):
        self.data.append(constructor(task=task))

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
                print(f'{ind+1}. {task['Task']} ({task['Status']}: {operatorTime.showTime(task['Date'])})')

        print('----------------')

    def dropData(self):
        return self.data

    def importData(self, data_import):
        self.data = data_import

    def changeTask(self, num, new_task):
        adress = int(num) - 1
        self.data[adress] = constructor(task=new_task, status='Updated')