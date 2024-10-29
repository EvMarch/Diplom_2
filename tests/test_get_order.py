import requests
import allure
from endpoints import Endpoints
from urls_credits import Urls,  StatusCode, Order, TextResponse

class TestGetOrder:

    @allure.title('Проверка получения заказов конкретного пользователя с авторизацией')
    @allure.description('Отправляем запрос на получение заказов с предварительной авторизацией, создание заказа и получение списка')
    def test_create_order_authorization_success(self, create_new_user):
        user_token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': user_token}
        response_create_order = requests.post(Urls.BASE_URL + Endpoints.CREATE_ORDER, headers=headers, data=Order.VALID_HASH_INGREDIENT)
        response_get_order = requests.get(Urls.BASE_URL + Endpoints.GET_ORDERS_LIST, headers=headers)
        assert response_get_order.json()['success'] is True and response_get_order.status_code == StatusCode.OK

    @allure.title('Проверка получения заказов конкретного пользователя без авторизации')
    @allure.description('Отправляем запрос на получение заказов с предварительной авторизацией, создание заказа и получение списка')
    def test_create_order_without_authorization(self):
        response = requests.get(Urls.BASE_URL + Endpoints.GET_ORDERS_LIST)
        assert TextResponse.UNAUTHORIZED in response.text and StatusCode.UNAUTHORIZED
