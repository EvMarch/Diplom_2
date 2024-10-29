# ручки API
class Endpoints:
    CREATE_USER = "/api/auth/register"  # Создание пользователя
    LOGIN_USER = "/api/auth/login"  # Логин пользователя в системе
    UPDATE_USER = "/api/auth/user" # Изменение данных пользователя
    DELETE_USER = "/api/auth/user" # удаление пользователя
    CREATE_ORDER = "/api/orders"  # Создание заказа
    GET_ORDERS_LIST = "/api/orders"  # Получение списка заказов пользователя




   # Получение заказов конкретного пользователя:

  #  авторизованный пользователь,
  #  неавторизованный пользователь.