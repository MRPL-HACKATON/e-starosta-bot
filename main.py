import telegram.ext
import telegram
import commands
import actions

updater = telegram.ext.Updater(token='1268566471:AAE7fq9_xyFcy_dFruyz_Fbmrzu2prX2yHY', use_context=True)
dispatcher = updater.dispatcher


def handle_callback_query(update, context):
	"""
	Сюда летят все команды (все, что было отправлено начиная с слеша /)

	:param update:
	:param context:
	:return:
	"""
	query = update.callback_query
	[action, value] = parse_callback_data(query.data)

	if action == 'choose_faculty_action':
		actions.choose_faculty_action(update, context, query, value)
	elif action == 'choose_group_action':
		actions.choose_group_action(update, context, query, value)
	elif action == 'choose_year_action':
		actions.choose_year_action(update, context, query, value)


def parse_callback_data(data):
	"""
	Парсим callback_data из callback_query. Ранее сформировали как action=value

	:param data:
	:return:
	"""
	return str(data).split(commands.ACTION_SEPARATOR)


# dispatcher.add_handler(telegram.ext.CommandHandler('start', commands.start))
dispatcher.add_handler(telegram.ext.CommandHandler('start', commands.choose_faculty))
dispatcher.add_handler(telegram.ext.CommandHandler('changetable', commands.change_table))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Filters.text('Отписаться от обновлений'), commands.unsubscribe))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Filters.text('Настроить заново'), commands.choose_faculty))

dispatcher.add_handler(telegram.ext.CallbackQueryHandler(handle_callback_query))

updater.start_polling()

