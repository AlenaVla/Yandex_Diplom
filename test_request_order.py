# Елена Куканова, 23-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# проверка того, что созданный заказ можно получить по номеру трека
def test_get_order():
    response = sender_stand_request.post_order()
    track = response.json()["track"]

    get_response = sender_stand_request.get_order(track)
    assert get_response.status_code == 200


