"""
    Для работы с ботом используется библиотека pyTelegramBotAPI

    pip install pyTelegramBotAPI

    Создание бота.
        bot = TeleBot(TOKEN)

    Основные методы бота.
    - отправка сообщения
        bot.send_message(chat_id, text)
    - отправка ответа на сообщение пользователя
        bot.reply_to(message, text)
    - регистрация функции, которая будет обрабатывать следующее сообщение
        bot.register_next_step_handler(message, next_step, *args, **kwargs)

    Функция, которая обрабатывает команду/сообщение принимает объект сообщения,
    в котором хранится вся информация о сообщении, авторе, чате и т.д.
"""

import telebot
from datetime import datetime
from random import randint
from string import ascii_letters, digits

from random import choice

from telebot import TeleBot

TOKEN = "1517223699:AAG0V9Tgz_fuaxiG6q3-3WiOAy_6sqfGRpc"
bot = TeleBot(TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/gen', '/magic')


@bot.message_handler(commands=["gen"])
def bot_gen_password(message):
    """Функция обрабатывает команду /gen
    Генерирует случайный пароль и отправляет его в чат
    """
    password = gen_password(ascii_letters + digits)
    bot.send_message(message.chat.id, password)


def gen_password(chars, length=8):
    password = ""
    for i in range(length):
        password += choice(chars)
    return password


@bot.message_handler(commands=["start", "first"])
def send_welcome(message):
    """Функция выполняется при командах /start и /first
    И отправляет сообщение в чат, с которого была получена команда
    """
    bot.send_message(message.chat.id, "Welcome!", reply_markup=keyboard1)


@bot.message_handler(commands=["hi"])
def send_welcome1(message):
    bot.send_message(message.chat.id, "Choose game", reply_markup=keyboard1)


@bot.message_handler(commands=["time"])
def send_time(message):
    """Функция выполняется при вводе команды /time
    Отправляет сообщение с текущей датой и временем
    Отвечает на команду сообщением с текущей датой и временем
    """
    time = datetime.now()  # возвращает текущую дату и время
    bot.send_message(message.chat.id, time)
    bot.reply_to(message, time)


@bot.message_handler(commands=["magic"])
def magic_game(message):
    """Функция генерирует случайно число
    Отвечает на команду сообщением.
    Регистрирует обработчик следующего сообщения - функцию _step
    """
    magic = randint(1, 10)
    msg = bot.reply_to(message, "The game started. Guess the number.")
    bot.register_next_step_handler(msg, _step, magic)


def _step(message, magic, counter=0):
    try:
        number = int(message.text)
        counter += 1
    except ValueError:
        bot.send_message(message.chat.id, "That's not a number.")
        return bot.register_next_step_handler(message, _step, magic, counter)

    if number > magic:
        bot.reply_to(message, "No, magic number less. Try again.")
        bot.register_next_step_handler(message, _step, magic, counter)
    elif number < magic:
        bot.reply_to(message, "No, magic number greater. Try again.")
        bot.register_next_step_handler(message, _step, magic, counter)
    else:
        text = (
            f"Congratulations! Magic number is {number}"
            f"\nAttempts: {counter}"
        )
        bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def echo_all(message):
    """Отвечает на все сообщения тем же текстом"""
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    print(message)


if __name__ == "__main__":
    print("bot is on now")
    bot.polling()
    print("bot is off")
