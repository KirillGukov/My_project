from telebot import types
import telebot

bot = telebot.TeleBot('6090083831:AAFMGwDuxORTUkGpMyciH53rUf6UqCqka8E')


@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup()
    results = types.KeyboardButton("Show results")
    markup.row(results)
    create = types.KeyboardButton("Create programm")
    train = types.KeyboardButton("Start training")
    markup.row(create, train)
    bot.send_message(message.chat.id, '<b>Choose your destiny!</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Show results':
        bot.send_message(message.chat.id, 'Your olympic results')
    if message.text == 'Create programm':
        bot.send_message(message.chat.id, 'Creating your personal programm')
    if message.text == 'Start training':
        bot.send_message(message.chat.id, 'Start your best train')




bot.polling(none_stop=True)
