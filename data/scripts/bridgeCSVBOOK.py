from data.scripts.workTime import giveTime

def constructor(task, date=None, status='Created'):
    if date is None:
        date = giveTime()
    return {
        'Date': date,
        'Task': task,
        'Status': status
    }