import allure
import pytest
import requests
#from couriers_requests import DataCourier
from endpoints import Endpoints
from helpers import TextResponse, StatusCode
from urls import Urls


class TestCreateUser:

    @allure.title('Проверка Создание пользователя')
    @allure.description('Отправляем запрос на создать уникального пользователя, проверяем ответ и удаляем созданного пользователя')
    def test_registration_user_success(self, create_new_user):
        user_data = create_new_user
        assert user_data[1].json().get("success") == True and user_data[1].status_code == StatusCode.OK


    @allure.title('Проверка нельзя создать пользователя, который уже зарегистрирован')
    @allure.description('Отправляем повторный запрос на создание пользователя, проверяем ответ и удаляем пользователя')
    def test_registration_double_user_failed(self, create_new_user):
        user_data = create_new_user
        payload = user_data[0]
        double_user_data = requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', data=payload)
        assert (double_user_data.status_code == StatusCode.FORBIDDEN) and (TextResponse.CREATE_DOUBLE_USER in double_user_data.text)





 #   @allure.title('Проверка чтобы создать курьера, нужно передать в ручку все обязательные поля Login/Password')
 #   @allure.description('Отправляем запрос на создание курьера без заполнения обязательных полей Login/Password и проверяем ответ')
 #   @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
       #                                    DataCourier.invalid_data_login_without_password])
  #  def test_courier_registration_without_parameters_failed(self, courier_data):
  #      response = requests.post(f'{Urls.BASE_URL}{Endpoints.create_courier}', data=courier_data)
  #      assert response.status_code == 400
   #     assert DataTextAnswer.need_more_data_sign in response.text


        # создать пользователя, который уже зарегистрирован;
        # создать пользователя и не заполнить одно из обязательных полей.