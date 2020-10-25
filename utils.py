import datetime
import bots

EXCLUDE_DAY = 'SUNDAY'

subscribers = {}

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
    return faculty.keys()


def get_all_groups():
    groups = []
    for facultet in faculty:
        groups = groups + faculty[facultet]
    return groups


def get_groups(facultet):
    return faculty[facultet]


def get_by_group_for_date(group, day):
    return schedule[group][day]


def find_facultet_for_group(group):
    facultet = None
    for facultet in faculty:
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
    # set has_change -> False
    return


def changeDaySchedule(group, day, lesson_num, lesson_name):
    # set has_change -> True
    return


def get_needed_day():
    """
    Получаем день, для которого нужно отдать расписание

    :return:
    """
    day = datetime.datetime.today().strftime('%A').upper()
    if day == EXCLUDE_DAY:
        return 'MONDAY'
    return day


def format_timetable(lessons, day):
    """
    Формирует нормальный вывод в текст

    :param lessons:
    :param day:
    :return:
    """
    text = "Расписание на " + day + "\n"
    for key, name in lessons.items():
        if key == 'has_changes':
            continue
        text += key + ": " + name + "\n"
    return text


def subscribe(group, chat_id):
    """
    Добавляет пользователя в список подписок для конкретной группы

    :param group:
    :param chat_id:
    :return:
    """
    if group not in subscribers:
        subscribers[group] = []
    subscribers[group].append(chat_id)


def notify(group, day):
    """
    Формирует список пар для конкретной группы и дня.
    Оповещает всех, кто подписан на эту группу
    
    :param group:
    :param day:
    :return:
    """
    lessons = get_by_group_for_date(group, day)
    text = format_timetable(lessons, day)
    if group not in subscribers:
        return
    for chat_id in subscribers[group]:
        bots.bot.send_message(chat_id=chat_id, text=text)
