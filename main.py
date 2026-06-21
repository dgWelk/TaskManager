from itertools import dropwhile

from data.classes.TaskBook import TaskBook
from data.classes.workCSV import workCSV
from data.scripts.clearConsole import clearConsole
from data.classes.workJson import workJson

operatorCSV = workCSV()
operatorJson = workJson()
app = TaskBook(operatorCSV.readCSV(), operatorJson.readJson())

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
                operatorCSV.writeCSV(app.dropData())
                print('Process of saved data is done.')
            elif choice == '6':
                #Settings Menu
                clearConsole()
                menu = 'settings'
            elif choice == '0':
                #Exit
                clearConsole()
                operatorCSV.writeCSV(app.dropData())
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
                menu = 'settingsTime'
                clearConsole()
            elif choice == '9':
                #Go to main menu
                clearConsole()
                menu = 'main'
            elif choice == '0':
                #Exit
                clearConsole()
                operatorCSV.writeCSV(app.dropData())
                break
            else:
                #Retry
                clearConsole()
                print('Error of input data. Try again.')

        elif menu == 'settingsTime':
            print(app.settingsTimeMenu)

            choice = input('chose the way >>> ')

            if choice == '1':
                #Change day format
                work = input('(On/Off)\nInput work >>> ')
                operatorJson.changeSettingsTime('dayFormat', work)
                clearConsole()
            elif choice == '2':
                # Change month format
                work = input('(On/Off)\nInput work >>> ')
                if work == 'Off':
                    type = input('(name/number)\nInput type >>> ')
                    operatorJson.changeSettingsTime('yearFormat', work, type)
                operatorJson.changeSettingsTime('yearFormat', work)
                clearConsole()
            elif choice == '3':
                # Change year format
                work = input('(On/Off)\nInput work >>> ')
                if work == 'Off':
                    type = input('(half/all)\nInput type >>> ')
                    operatorJson.changeSettingsTime('yearFormat', work, type)
                operatorJson.changeSettingsTime('yearFormat', work)
                clearConsole()
            elif choice == '4':
                # Change hour format
                work = input('(On/Off)\nInput work >>> ')
                if work == 'Off':
                    type = input('(AM/PM)\nInput type >>> ')
                    operatorJson.changeSettingsTime('yearFormat', work, type)
                operatorJson.changeSettingsTime('yearFormat', work)
                clearConsole()
            elif choice == '5':
                # Change minute format
                work = input('(On/Off)\nInput work >>> ')
                operatorJson.changeSettingsTime('monthFormat', work)
                clearConsole()
            elif choice == '6':
                # Change second format
                work = input('(On/Off)\nInput work >>> ')
                operatorJson.changeSettingsTime('monthFormat', work)
                clearConsole()
            elif choice == '9':
                # Go to settings menu
                clearConsole()
                menu = 'settings'
            elif choice == '0':
                # Exit
                clearConsole()
                operatorCSV.writeCSV(app.dropData())
                break
            else:
                # Retry
                clearConsole()
                print('Error of input data. Try again.')


def main():
    appWork()

main()
