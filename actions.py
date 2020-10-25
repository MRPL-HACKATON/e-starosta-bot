import utils
import db_utils
import telegram

ACTION_SEPARATOR = '='

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


def choose_faculty_action(update, context, query, faculty):
    chat_id = query['message']['chat_id']
    message_id = query['message']['message_id']
    keyboard = []
    for group in db_utils.getAllGroupsOfFaculty(faculty):
        callback_data = 'choose_group_action' + ACTION_SEPARATOR + group
        keyboard.append([telegram.InlineKeyboardButton(group, callback_data=callback_data)])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    context.bot.send_message(chat_id=chat_id, text='Теперь мне нужно узнать твю группу', reply_markup=reply_markup)


def choose_group_action(update, context, query, group):
    chat_id = query['message']['chat_id']
    message_id = query['message']['message_id']
    db_utils.subscribeUser(group, chat_id)
    day = utils.get_needed_day()
    lessons = db_utils.get_lessons_by_group_for_day(group, day)
    text = "No data"
    if lessons:
        text = utils.format_timetable(group, lessons, day)
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    context.bot.send_message(chat_id=chat_id, text=text)
