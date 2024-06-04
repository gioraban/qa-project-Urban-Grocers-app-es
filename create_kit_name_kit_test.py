import sender_stand_request
import data


def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201


def negative_assert_symbol(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos. " \
                                         "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"


def test_create_1_character_new_kit_body_get_success_response():
    positive_assert(data.kit1)


def test_create_511_character_new_kit_body_get_success_response():
    positive_assert(data.kit2)


def test_create_0_character_new_kit_body_get_error_response():
    negative_assert_symbol(data.kit3)
#error (expeted:400 / actual: 201)/ En Postman tambien funciona

def test_create_512_new_kit_body_error_response():
    negative_assert_symbol(data.kit4)
#error (expeted:400 / actual: 201) En Postman tambien funciona

def test_create_special_character_new_kit_body_get_success_response():
    positive_assert(data.kit5)
#No funciona en Postman

def test_create_space_new_kit_body_get_success_response():
    positive_assert(data.kit6)


def test_create_number_new_kit_body_get_success_response():
    positive_assert(data.kit7)


def test_create_not_params_new_kit_body_get_error_response():
    negative_assert_symbol(data.kit8)
#error (expeted:400 / actual: 500) Postman 500

def test_create_number_new_kit_body_get_error_response():
    negative_assert_symbol(data.kit9)
#error (expeted:400 / actual: 201) Postman 201









