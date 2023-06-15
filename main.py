
# При написании бота необходимо использовать библиотеку pytelegrambotapi.
import telebot # pip install pyTelegramBotAPI

from extensions import APIException, Api

# Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
from config import TG_TOKEN




bot = telebot.TeleBot(TG_TOKEN)


# При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
@bot.message_handler(commands=["start", "help"])
def start_help(message): # Название функции не играет никакой роли
    bot.reply_to(message,"""available commands:
    /values - all currencies
    <ccy1> <ccy2> <n> - how much <ccy2> need to buy <n> <ccy1>
    """)
# При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
@bot.message_handler(commands=["values"])
def values(message): 
    
    bot.reply_to(message,"qqq")


@bot.message_handler(content_types=["text"])
def convert(message:telebot.types.Message): 
# Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
# Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
    try:
        base, quote, n = parse_message(message.text.upper())
        bot.send_message(message.chat.id, Api.get_price(base, quote, n ))
# При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
    except APIException as e:
# Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
        bot.send_message(message.chat.id, "error: " + e.msg)

def parse_message(s:str)->tuple[str,str,float]:
    try:
        base, quote, n= s.split()
        n = float(n)
        return  base, quote, n
    except Exception as e:
        raise APIException(str(e))
if __name__ == '__main__':
     bot.infinity_polling()
