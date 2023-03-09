import telebot
from valute_config import keys, TOKEN
from valute_utils import ConvertionExeption, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n <имя валюты>' \
           '<в какую валюту перевести>' \
           '<количество переводимой валюты> \n Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    value = message.text.split(' ')

    if len(value) != 3:
        raise ConvertionExeption('Слишком много параметров.')

    quote, base, amount = value
    total_base = CryptoConverter.convert(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
