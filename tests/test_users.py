import allure
from data import EXISTING_USER, EXISTING_USER_MESSAGE, NO_REQUIRED_FIELD_MESSAGE

class TestCreateUser:
    @allure.title("Успешное создание пользователя")
    @allure.description("Проверка успешного создания пользователя")
    def test_create_user(self, user_data, user_methods):
        response = user_data[0]
        print(response.text)
        assert response.status_code == 200 and "true" in response.text

    @allure.title("Создание пользователя, который уже существует в системе")
    @allure.description("Проверка невозможности создания пользователя, который уже существует в системе")
    def test_create_exist_user(self, user_methods):
        response = user_methods.post_create_user(EXISTING_USER)
        assert response.status_code == 403 and response.json()['message'] == EXISTING_USER_MESSAGE

    @allure.title("Создание пользователя, заполняя не все обязательные поля")
    @allure.description("Проверка невозможности создания курьера, если не передать в запрос пароль")
    def test_create_user_without_password(self, user_data, user_methods):
        response = user_data[1]
        print(response.text)
        assert response.status_code == 403 and response.json()['message'] == NO_REQUIRED_FIELD_MESSAGE



