from faker import Faker

class DataCreate:
    # функция генерации фэйковых валидных данных
    @staticmethod
    def generating_fake_valid_data_to_create_user():
        fake = Faker('ru_RU')
        data = {
            "email": fake.email(),
            "name": fake.name(),
            "password": fake.password()
        }

        return data

    # функция генерации фэйковых данных без поля "Email"
    @staticmethod
    def generating_fake_invalid_data_to_create_user_without_email_field():
        fake = Faker("ru_RU")
        data = {
            "email": "",
            "name": fake.name(),
            "password": fake.password()
        }

        return data

    # функция генерации фэйковых данных без поля "Login"
    @staticmethod
    def generating_fake_invalid_data_to_create_user_without_name_field():
        fake = Faker("ru_RU")
        data = {
            "email": fake.email(),
            "name": "",
            "password": fake.password()
        }

        return data

    # функция генерации фэйковых данных без поля "Password"
    @staticmethod
    def generating_fake_invalid_data_to_create_user_without_password_field():
        fake = Faker("ru_RU")
        data = {
            "email": fake.email(),
            "name": fake.name(),
            "password": ""
        }

        return data

class StatusCode:

    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500

class TextResponse:
    CREATE_DOUBLE_USER = 'User already exists'
    SERVER_ERROR = 'Internal Server Error'
    UNAUTHORIZED = 'You should be authorised'
    CREATE_USER_ERROR = 'Email, password and name are required fields'
    INGREDIENTS = 'Ingredient ids must be provided'

class UserData:
    VALID_USER_DATA = {
        "email": "test-data@yandex.ru",
        "password": "password"
    }

    INVALID_USER_DATA = {
            "email": "invaliduser@example.com",
            "password": "wrongpassword"
    }

class Order:

    VALID_HASH_INGREDIENT = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }


    INVALID_HASH_INGREDIENT = {
        "ingredients": ["1234567abcdefg6jt544sd", "87654321abcdef9832kj3458"]
        }
