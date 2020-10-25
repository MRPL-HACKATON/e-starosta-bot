import utils
import db_utils

def set_group(query, context, value):
    """
    Сохраняем чат в подписки.
    Отправляем расписание.

    :param query:
    :param context:
    :param value:
    :return:
    """
    group = value
    chat_id = query['message']['chat_id']

    db_utils.subscribeUser(group, chat_id)

    # utils.subscribe(group, chat_id)  # подписка на обновления
    day = utils.get_needed_day()  # получение необходимого дня для расписания
    lessons = db_utils.get_lessons_by_group_for_day(group, day)
    # lessons = utils.get_by_group_for_date(group, day)  # получение расписания
    text = "No data"  # преобразование в строку
    if lessons:
        text = utils.format_timetable(group, lessons, day)

    context.bot.send_message(chat_id=chat_id, text=text)
