import configuration
import requests
import data


def post_new_user(body):  #funcion para crear un nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_user_token(): #funcion para extraer el token de autorizacion necesario ara crear el kit
    user_token = post_new_user(data.user_body)
    user_json = user_token.json()
    auth_token = user_json['authToken']
    return auth_token


def post_new_client_kit(kit_body):  #funcion para crear el kit
    token = get_user_token()
    heathers = data.headers.copy()   #funcion copy para no generar cambios de origen
    heathers['Authorization'] = f"Bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=heathers)
