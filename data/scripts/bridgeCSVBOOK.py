from data.scripts.workTime import giveTime


def constructor(date, data):
    return {
        'Date': date,
        'Task': data
    }

def CSVBOOK(data):
    result = []

    date = giveTime()

    for piece in data:
        result.append(constructor(date, piece))


CSVBOOK('asd')