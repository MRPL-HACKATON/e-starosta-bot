faculty = {
    'Информатика': ['КБ-001', 'КБ-002'],
    'Туризм': ['ТР-001', 'ТР-002']
}

schedule = {
    'КБ-001': {
        'MONDAY': {
            '1': 'Информатика',
            '2': 'Математика',
            '3': '',
            '4': ''
        },
        'TUESDAY': {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'WEDNESDAY': {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'THURSDAY': {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'FRIDAY': {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'SATURDAY': {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
    },
    'КБ-002': {
        'MONDAY': {
            'has_changes': False,
            '1': 'Информатика',
            '2': 'Математика',
            '3': '',
            '4': ''
        },
        'TUESDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'WEDNESDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'THURSDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'FRIDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'SATURDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
    },
    'ТР-001': {
        'MONDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'TUESDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'WEDNESDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'THURSDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'FRIDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'SATURDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
    },
    'ТР-002': {
        'MONDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'TUESDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'WEDNESDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'THURSDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'FRIDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        },
        'SATURDAY': {
            'has_changes': False,
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
    },

}

change_list = {
    'КБ-001': [],
    'КБ-002': [],
    'ТР-001': [],
    'ТР-002': []
}

assigns_users = {
    'КБ-001': [],
    'КБ-002': [],
    'ТР-001': [],
    'ТР-002': []
}


def get_facultets():
    return data.keys()


def get_all_groups():
    groups = []
    for facultet in data:
        groups = groups + list(data[facultet].keys())
    return groups


def get_groups(facultet):
    return data[facultet]


def get_by_group_for_date(group, date):
    facultet = find_facultet_for_group(group)
    return data[facultet][group][date]


def find_facultet_for_group(group):
    facultet = None
    for facultet in data:
        if group in facultet:
            facultet = facultet
            break

    return facultet

def getChanges():
    return {
        'group': ['MONDAY']
    }

def getDaySchedule(group, day):
    return {
        '1': 'First lesson',
        '2': 'Second lesson',
        '3': '',
        '4': ''
    }

def uncheckChange(group, day):
    #set has_change -> False
    return

def changeDaySchedule(group, day, lesson_num, lesson_name):
    # set has_change -> True
    return 
