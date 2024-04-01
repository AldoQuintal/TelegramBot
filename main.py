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
def consulta_inventario(message):
    tank_txt = ""
    print("### recibió el msj de inventario")
    try:
        response = requests.get(url=api_inv,auth=None,verify=False)
        print(f'Response: {response}')
        if response.status_code == 200:
            tanques = response.json()
            print(f'json_response: {tanques}')
            for tank in tanques:
                
                tank_txt += "Tanque: " + tank['vr_tanque'] + "\n" + "Fecha: " + tank['vr_fecha'] + "\n" + "Volumen: " + tank['vr_volumen'] + "\n" + "Volumen CT: " + tank['vr_vol_ct'] + "\n" + "Agua: " + tank['vr_agua'] + "\n" + "Temperatura: " + tank['vr_temp'] + "\n" + "\n"

            bot.reply_to(message, tank_txt)
    
    except:
        bot.reply_to(message, "Tengo problemas para comunicarme con los tanques en este momento")
    

@bot.message_handler(commands=['entrega'])
def consulta_ultima_entrega(message):
    entrega_txt = ""
    print("### Recibió el msj de entrga")
    
    try:
        response = requests.get(url=api_entr,auth=None,verify=False)
        print(f'Response: {response}')
        if response.status_code == 200:
            entregas = response.json()
            print(f'Entregas en el response: {entregas}')
            for entrega in entregas:
                print(entrega)
            
            entrega_txt += "Tanque: " + entrega['vr_tanque'] + "\n" + "Fecha inicial: " + entrega['fecha_ini'] + "\n" + "Fecha final: " + entrega['fecha_fin'] + "\n" + "Volumen inicial: " + entrega['vol_ini'] + "\n" + "Volumen final: " + entrega['vol_fin'] + "\n" + "Volumen CT inicial: " + entrega['vol_ct_ini'] + "\n" + "Volumen CT final: " + entrega['vol_ct_fin'] + "\n" + "Agua inicial: " + entrega['agua_ini'] + "\n" + "Agua final: " + entrega['agua_fin'] + "\n" + "Temperatura inicial: " + entrega['temp_ini'] + "\n" + "Temperatura final: " + entrega['temp_fin'] + "\n" + "Aumento neto: " + entrega['aum_neto'] + "\n" + "Aumento bruto: " + entrega['aum_bruto'] + "\n" + "Clave de producto: " + entrega['clv_prd'] + "\n"
            
            bot.reply_to(message, entrega_txt)
    
    except:
        bot.reply_to(message, "Tengo problemas para comunicarme con los tanques en este momento")
        
    
bot.message_handler(commands=['help'])
def ayuda(message):
    entrega_txt = ""
    print("### Recibió el msj de ayuda")
    
    bot.reply_to(message, "Utiliza los comandos de /inventario y /entrega para acceder a la info de los tanques")
    
    

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
    
if __name__ == "__main__":
    bot.polling(none_stop=True)