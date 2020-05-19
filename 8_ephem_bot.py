"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(update, bot):                  #Функция, отвечающая на /start
    text = 'Напишите /planet <planet_name>'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, bot):                  #Функция повторюшка
    user_text = update.message.text 
    print(user_text.split())
    update.message.reply_text(user_text)


def planet(update, bot):                      #Функция возвращает созвездие
    planet_name = update['message']['text'].split(' ')[1] # Вычленяю название планеты из update
    if planet_name == 'Mars':                             
        date = str(datetime.datetime.today())             # Сегодняшняя дата + время
        date = date.split(' ')[0].replace('-','/')        # Убираю время и привожу к нужному виду
        planet_loc = ephem.Mars(date)                     # Локация планеты в сегодняшний день
        planet_const = ephem.constellation(planet_loc)    # Название созввездия исходя из локации
        update.message.reply_text(f'{planet_name} сегодня в {planet_const}')      # Отвечаю в телеграм     
    else:
        update.message.reply_text('Попробуйте спросить про Марс')
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
