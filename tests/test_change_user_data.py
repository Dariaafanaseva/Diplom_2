import allure
from data import CHANGE_USER_DATA_NO_AUTHORISATION

class TestChangeUserData:
    @allure.title("Изменение данных пользователя с авторизацией")
    @allure.description("Проверка успешного изменения данных пользователя с авторизацией")
    def test_change_user_data_with_authorisation(self, user_data, user_methods):
        response = user_methods.patch_user_with_authorisation(user_data)
        print("Ответ API:", response.text)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.description("Проверка успешного изменения данных пользователя без авторизации")
    def test_change_user_data_without_authorisation(self, user_data, user_methods):
        response = user_methods.patch_user_without_authorisation(user_data)
        print("Ответ API:", response.text)
        assert response.status_code == 401 and response.json()['message'] == CHANGE_USER_DATA_NO_AUTHORISATION