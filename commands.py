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

