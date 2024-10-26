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
    def generating_fake_invalid_data_to_create_user_without_login_field():
        fake = Faker("ru_RU")
        data = {
            "email": fake.email(),
            "name": "",
            "password": fake.password()
        }

        return data

    # функция генерации фэйковых данных без поля "Password"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_password_field():
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
    CREATE_USER = '{"ok": true}'
    CREATE_DOUBLE_USER = 'User already exists'
    SERVER_ERROR = 'Internal Server Error'
    UNAUTHORIZED = 'You should be authorised'