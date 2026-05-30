from data.classes.TaskBook import TaskBook
from data.classes.workCSV import workCSV

operator = workCSV()
app = TaskBook(operator.readCSV())


def appWork():

    while True:

        print(app.menu)

        choice = input('chose the way >>> ')
        
        if choice == '1':
            app.addTask(input('Input ur new task >>> '))
        elif choice == '2':
            app.delTask(input('Input number of task >>> '))
        elif choice == '3':
            app.showTasks()
        elif choice == '4':
            operator.writeCSV(app.dropData())
            break
        else: print('Error of input data. Try again.')

def main():
    appWork()

main()


