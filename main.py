from data.classes.TaskBook import TaskBook
from data.classes.workCSV import workCSV
from data.scripts.clearConsole import clearConsole

operator = workCSV()
app = TaskBook(operator.readCSV())


def appWork():

    while True:

        print(app.menu)

        choice = input('chose the way >>> ')
        
        if choice == '1':
            app.addTask(input('Input ur new task >>> '))
            clearConsole()
        elif choice == '2':
            clearConsole()
            app.showTasks()
            app.changeTask(input('Input number of task >>> '), input('Input new task >>> '))
            clearConsole()
        elif choice == '3':
            clearConsole()
            app.showTasks()
            app.delTask(input('Input number of task >>> '))
            clearConsole()
        elif choice == '4':
            clearConsole()
            app.showTasks()
        elif choice == '5':
            clearConsole()
            operator.writeCSV(app.dropData())
            print('Process of saved data is done.')
        elif choice == '6':
            clearConsole()
            operator.writeCSV(app.dropData())
            break
        else:
            clearConsole()
            print('Error of input data. Try again.')


def main():
    appWork()

main()


