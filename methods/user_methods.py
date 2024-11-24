from data import USER_URL, LOGIN_URL, DELETE_USER_URL, CHANGE_USER_DATA_URL, USER_DATA_FOR_PATCH
import requests
import allure

class UserMethods:

    @allure.step("Создание пользователя")
    def post_create_user(self, params):
        response = requests.post(f'{USER_URL}', json=params)
        return response

    @allure.step("Авторизация пользователя")
    def post_login_user(self, params):
        response = requests.post(f'{LOGIN_URL}', json=params)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, user_data):
        response = requests.delete(f'{DELETE_USER_URL}', headers={'Authorization': user_data[2]})
        return response

    @allure.step("Изменение данных пользователя")
    def patch_user_with_authorisation(self, user_data):
        token = user_data[2].split(" ")[1]
        response = requests.patch(f'{CHANGE_USER_DATA_URL}', headers={'Authorization': f'Bearer {token}'}, json=USER_DATA_FOR_PATCH)
        return response

    @allure.step("Изменение данных пользователя без авторизации")
    def patch_user_without_authorisation(self):
        response = requests.patch(f'{CHANGE_USER_DATA_URL}',
                                  json=USER_DATA_FOR_PATCH)
        return response




