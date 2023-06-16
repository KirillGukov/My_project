from telebot import types
import telebot
from Project_telegram_bot.my_token import token

bot = telebot.TeleBot(token)


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
        bot.send_message(message.chat.id, 'Programm name:')

        @bot.message_handler()
        def programm_name(message):
            programm_name_dict = {}
            if message.text in programm_name_dict:
                bot.send_message(message.chat.id, 'Already exists')
            if message.text not in programm_name_dict:
                programm_name_dict[message] = message.from_user.id
                bot.send_message(message.chat.id, 'Created')

    if message.text == 'Start training':
        bot.send_message(message.chat.id, 'Start your best train')




bot.polling(none_stop=True)
