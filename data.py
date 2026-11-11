# Заголовки HTTP-запроса
CREATE_ORDER_HEADERS = {
    'Content-Type': 'application/json'
}
# Запрос создания заказа
CREATE_ORDER_PAYLOAD = {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Ivanovo 12",
    "metroStation": 4,
    "phone": "+7 903 460 37 83",
    "rentTime": 5,
    "deliveryDate": "2026-11-30",
    "comment": "Comment",
    "color": ["BLACK"]
}