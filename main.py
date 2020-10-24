from telegram.ext import *
from telegram import *
from datetime import datetime
from utils import *

updater = Updater(token='1268566471:AAE7fq9_xyFcy_dFruyz_Fbmrzu2prX2yHY', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
	keyboard = []
	for group in getAllGroups():
		callback_data = 'set_group=' + group
		keyboard.append([InlineKeyboardButton(group, callback_data=callback_data)])

	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Привет. Для начала мне нужно узнать твою группу', reply_markup=reply_markup)


def returnTimetable(update, context):
	query = update.callback_query
	group = str(query.data).split('=')[1]
	timetable = getTodayTimetable(group)
	update.message.reply_text(timetable) # тут валится, нет времени разбираться


def getTodayTimetable(group):
	today = datetime.today().strftime('%d.%m.%Y')
	return getByGroupForDate(group, today)


dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(returnTimetable))

updater.start_polling()

