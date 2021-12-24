import telebot
name = ''
bot = telebot.TeleBot("5055059862:AAHaFyA4d5OZpEDdebkPcP4O6ZyF2bu0zLo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "What?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text ==  'Привет':
		bot.reply_to(message, ' приветствую тебя обречённые на смерть '  )
	elif message.text ==  'пока':
		bot.reply_to(message, 'прошай ')
	elif message.text == '/reg':
		bot.send_message(message.from_user.id, 'как зовут обречённому на смерть?' )
	bot.register_next_step_handler(message,reg_name)

def reg_name(message):
	global name
	name = massage.text


bot.infinity_polling()
