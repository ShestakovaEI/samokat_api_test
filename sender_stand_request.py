import configuration
import requests
import data

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Получение трека заказа
def get_new_order_track():
    order_response = post_new_order(data.order_body)
    track = order_response.json()["track"]
    return track

# Получение заказа по треку
def get_order():
    track = get_new_order_track()
    params = data.order_params
    params["t"] = track
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=params)

