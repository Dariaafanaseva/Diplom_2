from data import ORDER_URL, INGREDIENT_URL
import requests
import allure

class OrderMethods:
    @allure.step("Создание заказа")
    def post_make_order(self, params, auth_header=None):
        headers = {}
        if auth_header:
            headers['Authorization'] = auth_header
        response = requests.post(f'{ORDER_URL}', json=params, headers=headers)
        return response

    @allure.step("Получение данных об ингредиентах")
    def get_ingredient(self):
        response = requests.get(f'{INGREDIENT_URL}')
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                ingredient_ids = [ingredient["_id"] for ingredient in data["data"]]
                if ingredient_ids:
                    first_ingredient = ingredient_ids[0]
                    last_ingredient = ingredient_ids[-1]
                    return {"ingredients": [first_ingredient, last_ingredient]}