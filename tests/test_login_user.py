import allure
import requests
from data.endpoints import Endpoints
from data.urls_credits import Urls, StatusCode, UserData, TextResponse

class TestLoginUser:

    @allure.title('Проверка пользователь может авторизоваться')
    @allure.description('Запрос на логин под существующим пользователем')
    def test_user_login_success(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN_USER}', json=UserData.VALID_USER_DATA)
        assert response.json()['success'] is True and response.status_code == StatusCode.OK

    @allure.title('Проверка авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Запрос на логин с неверным логином и паролем')
    def test_user_login_wrong_login_password_failed(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN_USER}', json=UserData.INVALID_USER_DATA)
        assert TextResponse.UNCORRECT in response.text and response.status_code == StatusCode.UNAUTHORIZED