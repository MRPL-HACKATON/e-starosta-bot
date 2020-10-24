from telegram.ext import Updater, CommandHandler

updater = Updater(token='1268566471:AAE7fq9_xyFcy_dFruyz_Fbmrzu2prX2yHY', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

