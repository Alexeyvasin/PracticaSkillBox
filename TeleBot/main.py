import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

def f_message(message):
    return True


@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, 'Hello world!')

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        if 'fuck' in message.text.lower():
            bot.reply_to(message, 'Не ругайся!')
        print(message)
        bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
