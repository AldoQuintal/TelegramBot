import telebot
import requests

TOKEN = '6820969878:AAHM9yHnZ_LQF_PS0kyWWWFqSdflweEx75g'

api_inv = 'http://localhost:8000/api/inventarios'
api_entr = 'http://localhost:8000/api/entregas'



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("### recibió el msj de start")
    response = requests.get(url=api_inv,auth=None,verify=False)
    print(f'Response: {response}')
    tanques = response.json()
    print(f'json_response: {tanques}')
    bot.reply_to(message, 'Hola bola')
    


@bot.message_handler(commands=['inventario'])
def send_welcome(message):
    tank_txt = ""
    print("### recibió el msj de start")
    response = requests.get(url=api_inv,auth=None,verify=False)
    print(f'Response: {response}')
    if response == 200:
        tanques = response.json()
        print(f'json_response: {tanques}')
        for tank in tanques:
            
            tank_txt += "Tanque: " + tank['vr_tanque'] + "\n" + "Fecha: " + tank['vr_fecha'] + "\n" + "Volumen: " + tank['vr_volumen'] + "\n" + "Volumen CT: " + tank['vr_vol_ct'] + "\n" + "Agua: " + tank['vr_agua'] + "\n" + "Temperatura: " + tank['vr_temp'] + "\n" + "\n"

        bot.reply_to(message, tank_txt)
    
    else:
        bot.reply_to(message, "Tengo problemas para comunicarme con los tanques en este momento")
    
        
    

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
    
if __name__ == "__main__":
    bot.polling(none_stop=True)