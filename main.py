from telegram.ext import *
from telegram import *
from datetime import datetime
from utils import *

updater = Updater(token='1268566471:AAE7fq9_xyFcy_dFruyz_Fbmrzu2prX2yHY', use_context=True)
dispatcher = updater.dispatcher

subscribers = {}


def subscribe(group, chat_id):
	if group not in subscribers:
		subscribers[group] = []
	subscribers[group].append(chat_id)


def start(update, context):
	keyboard = []
	for group in get_all_groups():
		callback_data = 'set_group=' + group
		keyboard.append([InlineKeyboardButton(group, callback_data=callback_data)])

	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Привет. Для начала мне нужно узнать твою группу', reply_markup=reply_markup)


def return_timetable(update, context):
	query = update.callback_query
	chat_id = query['message']['chat_id']
	group = str(query.data).split('=')[1]
	subscribe(group, chat_id)
	timetable = get_today_timetable(group)
	text = "Расписание на сегодня\n"
	for time, name in timetable.items():
		text += time + ": " + name + "\n"
	context.bot.send_message(chat_id=chat_id, text=text)


def get_today_timetable(group):
	today = datetime.today().strftime('%d.%m.%Y')
	return get_by_group_for_date(group, today)

dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(return_timetable))

updater.start_polling()

