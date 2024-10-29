import pytest
import requests

from helpers import DataCreate
from urls_credits import Urls
from endpoints import Endpoints


# Фикстура создания / удаления пользователя
@pytest.fixture
def create_new_user():
    payload = DataCreate.generating_fake_valid_data_to_create_user()
    response = requests.post(Urls.BASE_URL + Endpoints.CREATE_USER, json=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(Urls.BASE_URL + Endpoints.DELETE_USER, headers={"Authorization": token})


# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)

