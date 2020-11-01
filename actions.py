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

    day = utils.get_needed_day()  # получение необходимого дня для расписания
    lessons = db_utils.get_lessons_by_group_for_day(group, day)
    text = "No data"  # преобразование в строку
    if lessons:
        text = utils.format_timetable(group, lessons, day)

    context.bot.send_message(chat_id=chat_id, text=text)


def choose_faculty_action(update, context, query, faculty):
    chat_id = query['message']['chat_id']
    message_id = query['message']['message_id']
    keyboard = []
    for group in db_utils.fac_db['faculties'][faculty]['specialities']:
        callback_data = 'choose_group_action' + ACTION_SEPARATOR + group
        keyboard.append([telegram.InlineKeyboardButton(db_utils.fac_db['faculties'][faculty]['specialities'][group]['name'], callback_data=callback_data)])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    context.bot.send_message(chat_id=chat_id, text=db_utils.choose_group_message, reply_markup=reply_markup)


def choose_year_action(update, context, query, group):
    chat_id = query['message']['chat_id']
    message_id = query['message']['message_id']
    day = utils.get_needed_day()
    lessons = db_utils.get_lessons_by_group_for_day(group, day)
    text = "На данный момент нет доступных данных о расписании для этой группы. \nЗагляните позже!"
    if lessons:
        db_utils.subscribeUser(group, chat_id)
        text = utils.format_timetable(group, lessons, day)
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        
        keyboard = []
        keyboard.append([telegram.KeyboardButton("Отписаться от обновлений")])
        reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
    elif lessons == None:
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        context.bot.send_message(chat_id=chat_id, text=text)
    


def choose_group_action(update, context, query, group):
    chat_id = query['message']['chat_id']
    message_id = query['message']['message_id']
    keyboard = []
    for year in db_utils.fac_db['faculties'][group[:3]]['specialities'][group]['groups']:
        callback_data = 'choose_year_action' + ACTION_SEPARATOR + year
        keyboard.append([telegram.InlineKeyboardButton(db_utils.fac_db['faculties'][group[:3]]['specialities'][group]['groups'][year], callback_data=callback_data)])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    context.bot.send_message(chat_id=chat_id, text=db_utils.choose_year_message, reply_markup=reply_markup)