import requests
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

url = 'http://api.openweathermap.org/data/2.5/weather'

api_weather = '6f977b1a27510f7b390e4282046ed985'
api_telegram = '1517223699:AAG0V9Tgz_fuaxiG6q3-3WiOAy_6sqfGRpc'

bot = telebot.TeleBot(api_telegram)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.username) + ',' + '\n' +
     'В каком городе ищем?')


@bot.message_handler(content_types=['text'])
def weather_send(message):
    s_city = message.text
    try:
        params = {'APPID': api_weather, 'q': s_city, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()

        bot.send_message(message.chat.id, "В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + " ℃" + "\n" +
                "Ощущается как" + str(float(weather['main']['feels_like'])) + "\n" +
                "Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" +
                "Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" +
                "Скорость ветра " + str(float(weather['wind']['speed'])) + " м/с" + "\n" +
                "Давление " + str(float(weather['main']['pressure'])) + "\n" +
                "Влажность " + str(float(weather['main']['humidity'])) + "\n" +
                "Видимость " + str(weather['visibility']) + "\n" +
                "Описание " + str(weather['weather'][0]["description"]) + "\n")

        if weather["main"]['temp'] < 0:
            bot.send_message(message.chat.id, "А тебе точно нужно куда-то идти?"+ "\n" + "Дома не так уж и плохо.")
        elif weather["main"]['temp'] < 10:
            bot.send_message(message.chat.id, "Сейчас холодно!")
        elif weather["main"]['temp'] < 20:
            bot.send_message(message.chat.id, "Сейчас прохладно!")
        elif weather["main"]['temp'] > 38:
            bot.send_message(message.chat.id, "Сейчас жарко!")
        else:
            bot.send_message(message.chat.id, "Сейчас отличная температура!")
    except Exception:
        bot.send_message(message.chat.id, "Город " + s_city + " не найден")


if __name__ == '__main__':
    bot.polling(none_stop=True)
