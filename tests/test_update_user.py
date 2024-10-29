import allure
import requests
from data.helpers import DataCreate
from data.endpoints import Endpoints
from data.urls_credits import StatusCode, Urls, TextResponse
import pytest

class TestUpdateUser:

    @allure.title('Проверка на изменение данных пользователя с авторизацией')
    @allure.description('Проверка успешного изменения данных пользователя с корректным токеном')
    @pytest.mark.parametrize('data', [DataCreate.generating_fake_valid_data_to_create_user()["name"],
                                      DataCreate.generating_fake_valid_data_to_create_user()["password"],
                                      DataCreate.generating_fake_valid_data_to_create_user()["email"]
    ])
    def test_update_user_authorization(self, create_new_user, data):
        user_token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': user_token}
        response = requests.patch(f'{Urls.BASE_URL}{Endpoints.UPDATE_USER}', data=data, headers=headers)
        assert response.json()['success'] is True and response.status_code == StatusCode.OK



    @allure.title('Проверка на изменение данных пользователя с авторизацией')
    @allure.description('Проверка успешного изменения данных пользователя с корректным токеном')
    @pytest.mark.parametrize('data', [DataCreate.generating_fake_valid_data_to_create_user()["name"],
                                      DataCreate.generating_fake_valid_data_to_create_user()["password"],
                                      DataCreate.generating_fake_valid_data_to_create_user()["email"]
    ])
    def test_update_user_authorization(self, data):
        response = requests.patch(f'{Urls.BASE_URL}{Endpoints.UPDATE_USER}', data=data)
        assert TextResponse.UNAUTHORIZED in response.text and StatusCode.UNAUTHORIZED