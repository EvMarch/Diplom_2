import allure
import requests
from helpers import StatusCode, UserData, DataCreate
from endpoints import Endpoints
from urls import Urls
import pytest

# Создание заказа:

#  с авторизацией,
#  без авторизации,
#  с ингредиентами,
#  без ингредиентов,
# с неверным хешем ингредиентов.