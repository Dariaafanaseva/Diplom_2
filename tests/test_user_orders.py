import allure
from data import GET_ORDERS_NO_AUTHORISATION

class TestMakeOrder:
    @allure.title("Успешное получение заказов пользователя")
    @allure.description("Проверка получения заказов пользователя с авторизацией")
    def test_make_order_with_authorisation(self, user_data, order_methods):
        response = order_methods.get_user_orders(user_data[2])
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Неуспешное получение заказов пользователя")
    @allure.description("Проверка получения заказов пользователя без авторизации")
    def test_make_order_no_authorisation(self, order_methods):
        response = order_methods.get_user_orders()
        assert response.status_code == 401 and response.json()['message'] == GET_ORDERS_NO_AUTHORISATION