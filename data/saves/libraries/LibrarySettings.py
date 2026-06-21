be = {
    'On': True,
    'Off': False
}
type_day = {}
type_month = [
    'name',
    'number'
]
type_year = [
    'half',
    'all'
]
type_hour = [
    'AM',
    'PM'
]
type_minute = {}
type_second = {}

autoSaveTime = str(60*10)

localization = [
    'English',
    'Russia'
]

settings = {
    'time': {
        'dayFormat': {
            'be': be,
            'type': type_day,
        },
        'monthFormat': {
            'be': be,
            'type': type_month
        },
        'yearFormat': {
            'be': be,
            'type': type_year
        },
        'hourFormat': {
            'be': be,
            'type': type_hour
        },
        'minuteFormat': {
            'be': be,
            'type': type_minute
        },
        'secondFormat': {
            'be': be,
            'type': type_second
        }
    },
    'autoSave': {
        'be': be,
        'time': autoSaveTime
    },
    'localization': localization
}

#print(settings['localization'])