# Альбина Ерещенко, 47-я когорта — Финальный проект. Инженер по тестированию плюс
#
# Тесты разделены по функциям:
#   - создание заказа        → test_create_order_*
#   - получение заказа       → test_get_order_*
# Каждый тест проверяет ровно одну вещь.
import pytest
from sender_stand_request import create_order, get_order


# Фикстуры (подготовка данных)

@pytest.fixture
def created_order_response():
    """Создаёт заказ и возвращает полный ответ (для тестов на создание)."""
    return create_order()


@pytest.fixture
def track(created_order_response):
    "Достаёт трек-номер из уже созданного заказа (для тестов на получение)."
    return created_order_response.json().get('track')


# Тесты на создание заказа

def test_create_order_returns_201(created_order_response):
    "Создание заказа возвращает код 201."
    assert created_order_response.status_code == 201, \
        "Ожидался код 201 при создании заказа"


def test_create_order_response_has_track(created_order_response):
    "В ответе на создание заказа присутствует непустое поле 'track'."
    track_number = created_order_response.json().get('track')
    assert track_number, "В ответе на создание заказа отсутствует поле 'track'"


#Тест на получение заказа

def test_get_order_by_track_returns_200(track):
    "Получение заказа по треку возвращает код 200."
    get_order_response = get_order(track)
    assert get_order_response.status_code == 200, \
        "Ошибка получения заказа по треку {track}"