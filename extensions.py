import requests
from config import API_KEY

# Все классы спрятать в файле extensions.py.

class APIException(Exception):
    def __init__(self, msg) -> None:
        super().__init__()
        self.msg = msg

# Для отправки запросов к API описать класс со статическим методом get_price(), который 
class Api:
    @classmethod
    def get_price(class_, base:str, quote:str, amount:float)->float:
        # принимает три аргумента и возвращает нужную сумму в валюте:
        # имя валюты, цену на которую надо узнать, — base;
        # имя валюты, цену в которой надо узнать, — quote;
        # количество переводимой валюты — amount.

        try:
            # Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.
            url = f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}"
            r = requests.get(url,headers={"authorization": "Apikey " + API_KEY})
            
            # Для парсинга полученных ответов использовать библиотеку JSON.
            data = r.json()
            return data[quote] * amount
        except Exception as e:
            raise APIException(str(e))