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


