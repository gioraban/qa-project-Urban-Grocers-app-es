import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_user_token():
    user_token = post_new_user(data.user_body)
    print(user_token)
    user_json = user_token.json()
    print(user_json)
    auth_token = user_json['authToken']
    print(auth_token)
    return auth_token


def post_new_client_kit(kit_body):
    token = get_user_token()
    heathers = data.headers.copy()
    heathers['Authorization'] = f"Bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=heathers)


response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())