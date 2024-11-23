import allure
from data import USER_DATA, INCORRECT_USER_DATA, INCORRECT_DATA_FOR_LOGIN_MESSAGE

class TestLoginUser:
    @allure.title("Успешная авторизация")
    @allure.description("Проверка авторизации существующего пользователя")
    def test_login_user(self, user_methods):
        response = user_methods.post_login_user(USER_DATA)
        assert response.status_code == 200 and "true" in response.text

    @allure.title("Неуспешная авторизация")
    @allure.description("Проверка авторизации с несуществующим пользователем")
    def test_login_user(self, user_methods):
        response = user_methods.post_login_user(INCORRECT_USER_DATA)
        assert response.status_code == 401 and response.json()['message'] == INCORRECT_DATA_FOR_LOGIN_MESSAGE

