import telebot
import requests

TOKEN = '6820969878:AAHM9yHnZ_LQF_PS0kyWWWFqSdflweEx75g'
url = 'https://10.10.208:8000/api/entregas'

api_inv = 'http://10.10.208:8000/api/inventarios'
api_entr = 'http://10.10.208:8000/api/entregas'



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    response = requests.get(url=api_inv,auth=None,verify=False)
    tanques = response.json()
    print(f'json_response: {tanques}')
    bot.reply_to(message, 'Hola bola')
        
    

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
    
if __name__ == "__main__":
    bot.polling(none_stop=True)