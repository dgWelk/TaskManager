import datetime
from os.path import exists

from data.classes.workJson import workJson

operatorJson = workJson()

class formatDate:
    def __init__(self):

        self.data = operatorJson.readJson()['time']

        self.months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]

        date = datetime.datetime.now().strftime('%d-%m-%Y')
        time = datetime.datetime.now().strftime('%H-%M-%S')

        self.dt = '-'.join([date, time])
        self.time = time


    def giveTime(self):
        return self.dt

    def showTime(self, input_time):

        time = input_time.split('-')

        lst_date = []
        lst_time = []

        isDay = self.data['dayFormat']['be'] == 'On'
        isMonth = self.data['monthFormat']['be'] == 'On'
        isYear = self.data['yearFormat']['be'] == 'On'
        isHour = self.data['hourFormat']['be'] == 'On'
        isMinute = self.data['minuteFormat']['be'] == 'On'
        isSecond = self.data['secondFormat']['be'] == 'On'


        if isDay:lst_date.append(time[0])
        if isMonth:
            if self.data['monthFormat']['type'] == 'number':
                lst_date.append(time[1])
            elif self.data['monthFormat']['type'] == 'name':
                lst_date.append(self.months[int(time[1])-1])
        if isYear:
            if self.data['yearFormat']['type'] == 'all':
                lst_date.append(time[2])
            elif self.data['yearFormat']['type'] == 'half':
                year = list(str(time[2]))
                year = ''.join(year[2:])
                lst_date.append(year)
        if isHour:
            if self.data['hourFormat']['type'] == 'AM':
                lst_time.append(time[3])
            elif self.data['hourFormat']['type'] == 'PM':
                if int(self.time[3])-12 >= 0:
                    lst_time.append(str(int(time[3])-12))
                else:
                    lst_time.append(time[3])
        if isMinute:lst_time.append(time[4])
        if isSecond:lst_time.append(time[5])

        if self.data['monthFormat']['be'] == 'On' and self.data['monthFormat']['type'] == 'name':date = ' '.join(lst_date)
        else:date = '.'.join(lst_date)
        out_time = ':'.join(lst_time)
        if self.data['hourFormat']['type'] == 'PM':out_time += ' PM'
        return f'{date} {out_time}'