import allure
from data import INCORRECT_INGREDIENT

class TestMakeOrder:
    @allure.title("Успешное создание заказа")
    @allure.description("Проверка успешного создания заказа без авторизации")
    def test_make_order_no_authorisation(self, order_methods):
        ingredient = order_methods.get_ingredient()
        response = order_methods.post_make_order(ingredient)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Успешное создание заказа с авторизацией")
    @allure.description("Проверка успешного создания заказа с ингредиентами с авторизацией")
    def test_make_order_with_authorisation(self, user_data, order_methods):
        ingredient = order_methods.get_ingredient()
        response = order_methods.post_make_order(ingredient, user_data[2])
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка неуспешного создания заказа без ингредиентов")
    def test_make_order_no_ingredients(self, user_data, order_methods):
        response = order_methods.post_make_order(user_data[2])
        assert response.status_code == 400

    @allure.title("Создание заказа с неверным хэшем ингредиента")
    @allure.description("Проверка неуспешного создания заказа с неверным хэшем ингредиентов")
    def test_make_order_incorrect_ingredient(self, user_data, order_methods):
        response = order_methods.post_make_order(INCORRECT_INGREDIENT, user_data[2])
        assert response.status_code == 500

