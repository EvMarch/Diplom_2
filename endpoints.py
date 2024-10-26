# ручки API
class Endpoints:
    CREATE_USER = "/api/auth/register"  # Создание пользователя
    LOGIN_USER = "/api/auth/login"  # Логин пользователя в системе
    UPDATE_USER = "/api/auth/user" # Изменение данных пользователя
    DELETE_USER = "/api/auth/user" # удаление пользователя
    CREATE_ORDER = "/api/orders"  # Создание заказа
    GET_ORDERS_LIST = "/api/orders"  # Получение списка заказов пользователя




  #  Изменение данных пользователя:
  #  с авторизацией,
  #  без авторизации,

  #  Для обеих ситуаций нужно проверить, что любое поле можно изменить.Для неавторизованного пользователя — ещё
  #  и то, что система вернёт ошибку.


   # Создание заказа:

  #  с авторизацией,
  #  без авторизации,
  #  с ингредиентами,
  #  без ингредиентов,
   # с неверным хешем ингредиентов.


   # Получение заказов конкретного пользователя:

  #  авторизованный пользователь,
  #  неавторизованный пользователь.