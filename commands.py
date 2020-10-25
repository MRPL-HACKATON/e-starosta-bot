import telegram
import utils
import db_utils

ACTION_SEPARATOR = '='


def start(update, context):
    """
    Обработка команды /start

    :param update:
    :param context:
    :return:
    """
    keyboard = []
    for group in db_utils.getAllGroups():
        callback_data = 'set_group' + ACTION_SEPARATOR + group
        keyboard.append([telegram.InlineKeyboardButton(group, callback_data=callback_data)])

    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет. Для начала мне нужно узнать твою группу', reply_markup=reply_markup)


def chooce_faculty(update, context):
    keyboard = []
    for faculty in db_utils.getAllFaculties():
        callback_data = 'choose_faculty_action' + ACTION_SEPARATOR + faculty
        keyboard.append([telegram.InlineKeyboardButton(faculty, callback_data=callback_data)])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(db_utils.start_message, reply_markup=reply_markup)

def unsubscribe(update, context):
    chat_id = update['message']['chat_id']
    db_utils.unsubscribeUser(chat_id)
    keyboard = []
    keyboard.append([telegram.KeyboardButton("/start")])
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=chat_id, text="До встречи 👏️", reply_markup=reply_markup)


def change_table(update, context):
    """
    Обработка команды /changetable
    Фейковая смена расписания с последующим оповещением об этом

    :param update:
    :param context:
    :return:
    """

    db_utils.random_update()
    utils.notify_all(db_utils.getPushList())
    db_utils.cleanChangeList()

