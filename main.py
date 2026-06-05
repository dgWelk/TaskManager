from data.classes.TaskBook import TaskBook
from data.classes.workCSV import workCSV
from data.scripts.clearConsole import clearConsole

operator = workCSV()
app = TaskBook(operator.readCSV())

def appWork():
    menu = 'main'
    while True:

        if menu == 'main':
            print(app.mainMenu)

            choice = input('chose the way >>> ')

            if choice == '1':
                #AddTask
                app.addTask(input('Input ur new task >>> '))
                clearConsole()
            elif choice == '2':
                #Change Task
                clearConsole()
                app.showTasks()
                app.changeTask(input('Input number of task >>> '), input('Input new task >>> '))
                clearConsole()
            elif choice == '3':
                #Delete Task
                clearConsole()
                app.showTasks()
                app.delTask(input('Input number of task >>> '))
                clearConsole()
            elif choice == '4':
                #Show Tasks
                clearConsole()
                app.showTasks()
            elif choice == '5':
                #Save
                clearConsole()
                operator.writeCSV(app.dropData())
                print('Process of saved data is done.')
            elif choice == '6':
                #Settings Menu
                clearConsole()
                menu = 'settings'
            elif choice == '0':
                #Exit
                clearConsole()
                operator.writeCSV(app.dropData())
                break
            else:
                #Retry
                clearConsole()
                print('Error of input data. Try again.')

        elif menu == 'settings':
            print(app.settingsMenu)

            choice = input('chose the way >>> ')

            if choice == '1':
                #Change time format
                clearConsole()
            elif choice == '9':
                #Go to main menu
                clearConsole()
                menu = 'main'
            elif choice == '0':
                #Exit
                clearConsole()
                operator.writeCSV(app.dropData())
                break
            else:
                #Retry
                clearConsole()
                print('Error of input data. Try again.')


def main():
    appWork()

main()


