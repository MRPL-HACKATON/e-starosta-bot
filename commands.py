import telegram
import utils

ACTION_SEPARATOR = '='


def start(update, context):
    """
    Обработка команды /start

    :param update:
    :param context:
    :return:
    """
    keyboard = []
    for group in utils.get_all_groups():
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
    change_lessons()  # заменить на смену расписания
    check()  # заменить на проверку изменения в расписании, определение группы и дня (возможно сменить реализацию)
    utils.notify('КБ-001', 'MONDAY')


def change_lessons():
    pass


def check():
    pass
