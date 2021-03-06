import datetime
import bots
import db_utils

EXCLUDE_DAY = 'SUNDAY'

DAY_MAPPER = {
    'MONDAY': 'Понедельник',
    'TUESDAY': 'Вторник',
    'WEDNESDAY': 'Среда',
    'THURSDAY': 'Четверг',
    'FRIDAY': 'Пятница',
    'SATURDAY': 'Суббота'
}

def get_needed_day():
    """
    Получаем день, для которого нужно отдать расписание

    :return:
    """
    day = datetime.datetime.today().strftime('%A').upper()
    if day == EXCLUDE_DAY:
        return 'MONDAY'
    return day


def format_timetable(group, lessons, day):
    """
    Формирует нормальный вывод в текст

    :param lessons:
    :param day:
    :return:
    """
    text = "Актуально на сегодня " + "\n" + db_utils.fac_db['faculties'][group[:3]]['specialities'][group[:-3]]['name']+', '+db_utils.fac_db['faculties'][group[:3]]['specialities'][group[:-3]]['groups'][group] + "\n" + DAY_MAPPER[day] + ":\n"
    for key, name in lessons.items():
        if key == 'has_changes':
            continue
        text += key + ": " + name + "\n"
    return text

def format_update_timetable(group, lessons, day):
    """
    Формирует нормальный вывод в текст

    :param lessons:
    :param day:
    :return:
    """
    text = db_utils.change_schedule_message + "\n" + db_utils.fac_db['faculties'][group[:3]]['specialities'][group[:-3]]['name']+', '+db_utils.fac_db['faculties'][group[:3]]['specialities'][group[:-3]]['groups'][group] + "\n" + DAY_MAPPER[day] + ":\n"
    for key, name in lessons.items():
        if key == 'has_changes':
            continue
        text += key + ": " + name + "\n"
    return text


def notify_all(push_list):
    for chat_id in push_list.keys():
        for day in push_list[chat_id].keys():
            text = format_update_timetable(db_utils.getGroupByUser(chat_id), push_list[chat_id][day], day)
            bots.bot.send_message(chat_id=chat_id, text=text)

