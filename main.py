import telebot
import random
from telebot import types

#Создаем бота
bot = telebot.TeleBot('5320339089:AAG0qabrmulHBlqpnqe6lUAMdynl8Dj7A0k')

#Загружаем список никнеймов
f = open('data/nickname.txt', 'r', encoding='UTF-8')
nickname = f.read().split('\n')
f.close()

#Загружаем список цитат
f = open('data/quote.txt', 'r', encoding='UTF-8')
quote  = f.read().split('\n')
f.close()

# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        #Добавляем 2 кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ник")
        item2=types.KeyboardButton("Цитата")
        markup.add(item1)
        markup.add(item2)
        #Приветствие
        bot.send_sticker(m.chat.id, "CAACAgQAAxkBAAEFC2piqQAC5g390ZTmw18peVckQ2bYggAC5mAAAuOnXQWcu2EHUgGSlSQE")
        bot.send_message(m.chat.id, 'Если гулю SSS+ ранга потребовался ник нажми: Ник \n а если нужна цитата из кодекса нажми Цитата',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Ник' :
            answer = random.choice(nickname)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Цитата':
            answer = random.choice(quote)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)