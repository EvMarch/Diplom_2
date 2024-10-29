import allure
import requests
from endpoints import Endpoints
from urls_credits import Urls,  StatusCode, Order, TextResponse

class TestOrderCreate:

    @allure.title('Проверка создания заказа с авторизацией с ингредиентами')
    @allure.description('Отправляем запрос на создание заказа с предварительной авторизацией и получением токена (валидный хэш ингредиентов)')
    def test_create_order_authorization_success(self, create_new_user):
        user_token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': user_token}
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}', data=Order.VALID_HASH_INGREDIENT, headers=headers)
        assert response.json()['success'] is True and response.status_code == StatusCode.OK

    @allure.title('Проверка создания заказа без авторизации с ингредиентами')
    @allure.description('Отправляем запрос на создание заказа без предварительной авторизации (валидный хэш ингредиентов)')
    def test_create_order_without_authorization_success(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}', data=Order.VALID_HASH_INGREDIENT)
        assert response.json()['success'] is True and response.status_code == StatusCode.OK

    @allure.title('Проверка создания заказа с авторизацией без ингредиентов')
    @allure.description(
        'Отправляем запрос на создание заказа с предварительной авторизацией и получением токена (пустой список ингредиентов)')
    def test_create_order_authorization_empty_hash(self, create_new_user):
        user_token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': user_token}
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}', data=[], headers=headers)
        assert TextResponse.INGREDIENTS in response.text and response.status_code == StatusCode.BAD_REQUEST

    @allure.title('Проверка создания заказа с авторизацией с невалидным хэшем')
    @allure.description('Отправляем запрос на создание заказа с предварительной авторизацией и получением токена (невалидный хэш ингредиентов)')
    def test_create_order_authorization_invalid_hash(self, create_new_user):
        user_token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': user_token}
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}', data=Order.INVALID_HASH_INGREDIENT, headers=headers)
        assert TextResponse.SERVER_ERROR in response.text and response.status_code == StatusCode.INTERNAL_SERVER_ERROR