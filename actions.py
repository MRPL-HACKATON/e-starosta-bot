import utils


def set_group(query, context, value):
    """
    Сохраняем чат в подписки.
    Отправляем расписание.
    :param query:
    :param context:
    :param data:
    :return:
    """
    group = value
    chat_id = query['message']['chat_id']
    utils.subscribe(group, chat_id)

    day = utils.get_needed_day()
    lessons = utils.get_by_group_for_date(group, day)
    text = utils.format_timetable(lessons, day)

    context.bot.send_message(chat_id=chat_id, text=text)
