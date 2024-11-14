import configuration
import requests
import data

# создает заказ
def post_order ():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)

# получает заказ по номеру
def get_order(t_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t":t_order})