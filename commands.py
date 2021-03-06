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
    for fac in db_utils.faculties:
        callback_data = 'set_group' + ACTION_SEPARATOR + group
        keyboard.append([telegram.InlineKeyboardButton(group, callback_data=callback_data)])

    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет. Для начала мне нужно узнать твою группу', reply_markup=reply_markup)


def choose_faculty(update, context):
    keyboard = []
    for faculty in db_utils.fac_db['faculties']:
        callback_data = 'choose_faculty_action' + ACTION_SEPARATOR + faculty
        keyboard.append([telegram.InlineKeyboardButton(db_utils.fac_db['faculties'][faculty]['name'], callback_data=callback_data)])
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(db_utils.start_message, reply_markup=reply_markup)

def unsubscribe(update, context):
    chat_id = update['message']['chat_id']
    db_utils.unsubscribeUser(chat_id)
    keyboard = []
    keyboard.append([telegram.KeyboardButton("Настроить заново")])
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=chat_id, text="Рассылка отключена. До встречи 👏️", reply_markup=reply_markup)


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

