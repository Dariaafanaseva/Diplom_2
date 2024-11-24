import pytest
import random
import string
from methods.user_methods import UserMethods
from methods.orders_methods import OrderMethods

@pytest.fixture()
def user_methods():
    return UserMethods()

@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture()
def user_data(user_methods):
    def generate_random_string(length=8):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    login = generate_random_string(6)
    password = generate_random_string(8)
    name = generate_random_string(6)

    domain = generate_random_string(5) + ".ru"
    email = f"{login}@{domain}"

    payload = {"email": email,
        "password": password,
        "name": name}

    response = user_methods.post_create_user(payload)
    print(f"Create user response: {response.text}")
    assert response.status_code == 200, "Не удалось создать пользователя"
    user_data = response.json()
    token = user_data.get("accessToken")

    no_password_payload = {"email": email,
        "name": name}
    no_password_response = user_methods.post_create_user(no_password_payload)
    print(f"no password response: {no_password_response.text}")
    yield response, no_password_response, token
    if token:
        user_methods.delete_user(token)
        print('Пользователь успешно удален')


