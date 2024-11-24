BASE_URL = 'https://stellarburgers.nomoreparties.site/'
USER_URL = f'{BASE_URL}/api/auth/register'
LOGIN_URL = f'{BASE_URL}/api/auth/login'
DELETE_USER_URL = f'{BASE_URL}/api/auth/user'
CHANGE_USER_DATA_URL = f'{BASE_URL}/api/auth/user'
ORDER_URL = f'{BASE_URL}/api/orders'
INGREDIENT_URL = f'{BASE_URL}/api/ingredients'


USER_DATA = {
"email": "AfanasevaDaria@ya.ru",
"password": "qwerty"}

INCORRECT_USER_DATA = {
"email": "Stukalo@ya.ru",
"password": "ytrewq"}

USER_DATA_FOR_PATCH = {"email": "Stukalov85633@ya.ru",
                                "name": "Masha"}

EXISTING_USER = {
"email": "AfanasevaDaria@ya.ru",
"password": "qwerty",
"name": "Daria"
}

INCORRECT_INGREDIENT = {
"ingredients": ["dacab0026a733c6","6e00276b2870"]}

EXISTING_USER_MESSAGE = 'User already exists'
NO_REQUIRED_FIELD_MESSAGE = 'Email, password and name are required fields'
INCORRECT_DATA_FOR_LOGIN_MESSAGE = 'email or password are incorrect'
CHANGE_USER_DATA_NO_AUTHORISATION = 'You should be authorised'
MAKE_ORDER_NO_INGREDIENTS = 'Ingredient ids must be provided'
GET_ORDERS_NO_AUTHORISATION = 'You should be authorised'


