import datetime

def giveTime():
    date = datetime.datetime.now().strftime('%d.%m.%Y')
    time = datetime.datetime.now().strftime('%H:%M')
    dt = ' '.join([date, time])
    return dt