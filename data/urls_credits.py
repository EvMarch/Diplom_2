class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

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
    UNCORRECT = 'email or password are incorrect'
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