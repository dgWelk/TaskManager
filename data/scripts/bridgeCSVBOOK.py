from data.classes.FormatDate import formatDate

operatorTime = formatDate

def constructor(task, date=None, status='Created'):
    if date is None:
        date = operatorTime().giveTime()
    return {
        'Date': date,
        'Task': task,
        'Status': status
    }