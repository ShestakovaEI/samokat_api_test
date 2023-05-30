import sender_stand_request

# Проверка, что код ответа равен 200
def test_get_order_info_get_success_response():
    response = sender_stand_request.get_order()
    assert response.status_code == 200