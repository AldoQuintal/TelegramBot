import telebot

TOKEN = '6820969878:AAHM9yHnZ_LQF_PS0kyWWWFqSdflweEx75g'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola bola')
    
    

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
    
if __name__ == "__main__":
    bot.polling(none_stop=True)