# Альбина Еоещенко, 47-я когорта — Финальный проект. Инженер по тестированию плюс
# Шаги автотеста:
# Выполнить запрос на создание заказа.
# Сохранить номер трека заказа.
# Выполнить запрос на получение заказа по треку заказа.
# Проверить, что код ответа равен 200.
from sender_stand_request import create_order, get_order
def test_get_order():
    create_order_response = create_order()
    assert create_order_response.status_code == 201, "Ошибка создания заказа. Необходимо проверить данные запроса"
    track = create_order_response.json().get('track')
    assert track, "В ответе на создание заказа отсутствует поле 'track'"
    get_order_response = get_order(track)
    assert get_order_response.status_code == 200, "Ошибка получения заказа {track}"
    print('Проверка пройдена!')
if __name__ == '__main__':
    test_get_order()