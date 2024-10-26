import allure
import pytest
import requests
from endpoints import Endpoints
from helpers import TextResponse, StatusCode, DataCreate
from urls import Urls


class TestCreateUser:

    @allure.title('Проверка Создание пользователя')
    @allure.description('Запрос на создание уникального пользователя, проверяем ответ')
    def test_registration_user_success(self, create_new_user):
        response = create_new_user
        assert response[1].json()['success'] is True and response[1].status_code == StatusCode.OK

    @allure.title('Проверка нельзя создать пользователя, который уже зарегистрирован')
    @allure.description('Повторный запрос на создание пользователя, проверяем ответ')
    def test_registration_double_user_failed(self, create_new_user):
        response = create_new_user
        payload = response[0]
        double_response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', data=payload)
        assert TextResponse.CREATE_DOUBLE_USER in double_response.text and double_response.status_code == StatusCode.FORBIDDEN




    @allure.title('Проверка создать пользователя и не заполнить одно из обязательных полей')
    @allure.description('Запрос на создание пользователя без заполнения обязательных полей проверяем ответ')
    @pytest.mark.parametrize('new_user', [DataCreate.generating_fake_invalid_data_to_create_user_without_email_field(),
                                           DataCreate.generating_fake_invalid_data_to_create_user_without_name_field(),
                                           DataCreate.generating_fake_invalid_data_to_create_user_without_password_field()])
    def test_registration_user_without_parameters_failed(self, new_user):
        #payload = create_new_user
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', json=new_user)
        assert TextResponse.CREATE_USER_ERROR in response.text and response.status_code == StatusCode.FORBIDDEN
