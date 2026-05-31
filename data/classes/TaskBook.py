from data.scripts.bridgeCSVBOOK import constructor

class TaskBook:
    def __init__(self, data_import):
        self.fieldnames = ['Date', 'Task']
        self.data = data_import if data_import else []

        self.version = 'b.0.3'

        self.menu = f'''----------------
Task Manager {self.version}
----- Menu -----
1. Add Task
2. Change Task
3. Delete Task
4. Show Tasks
5. Save Tasks
6. Exit
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
                print(f'{ind+1}. {task['Task']} ({task['Status']}: {task['Date']})')

        print('----------------')

    def dropData(self):
        return self.data

    def importData(self, data_import):
        self.data = data_import

    def changeTask(self, num, new_task):
        adress = int(num) - 1
        self.data[adress] = constructor(new_task, status='Updated')