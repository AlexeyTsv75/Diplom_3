import random

import allure
import requests
import data


@allure.step('Создаем случайный емейл')
def get_random_email():
    email = f'{random.choice(['alex', 'john', 'kean'])}.{random.randint(100, 999)}@mail.{random.choice(['net', 'com',
                                                                                                        'ru'])}'
    return email


@allure.step('Создаем данные случайного пользователя')
def get_random_user_payload():
    email = get_random_email()
    password = f'{random.randint(100000, 999999)}'
    name = f'{random.choice(['alex', 'john', 'kean'])}'
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


@allure.step('Создаем нового пользователя')
def new_user_creation():
    payload = get_random_user_payload()
    response = requests.post(data.URL_MAIN_PAGE+data.REGISTRATION, data=payload)
    payload["code"] = response.status_code
    payload["token"] = response.json()["accessToken"]
    payload["retoken"] = response.json()["refreshToken"]
    return payload


@allure.step('Удаляем пользователя')
def delete_user(token):
    requests.delete(data.URL_MAIN_PAGE+data.USER, headers={'Authorization': token})