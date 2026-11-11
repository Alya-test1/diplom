# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration
# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests
# Импортируем данные запроса
import data
# Создание заказа через POST и возвращаем объект ответа
def create_order():
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH
    response = requests.post(
        url,
        json=data.CREATE_ORDER_PAYLOAD,
        headers=data.CREATE_ORDER_HEADERS
    )
    print('Create order: статус {response.status_code}, тело: {response.text}')
    return response
# Для получения заказа по номеру трека отправляем GET запрос и возвращаем объект ответа
def get_order(track):
    url = configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH
    params = {'t': track}
    response = requests.get(url, params=params)
    print('Get order by track: статус {response.status_code}, тело: {response.text}')
    return response