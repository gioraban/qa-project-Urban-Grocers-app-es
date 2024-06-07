#  **Proyecto Urban Grocers** 

En este proyecto se trata de automatizar la lista de comprobacion del campo **name**  en la solicitud de creacion de un kit de productos. Para ello se necesita crear primero un usurio.

El primer paso es instalar en Pychart pip, piptest, request.
Segundo paso, enlazar la cuenta de GitHub Desktop a la plataforma de Tripleten a traves de la API que aparece en la entregada del proyecto Sprint 7.
Luego, ve a GitHub y clona el nombre del repositorio **qa-project-Urban-Grocers-app-es**  a la computadora local con los siguientes pasos:

1. Abre la linea de comandos en tu computadora.
2. Crea un directorio para almacenar todos tus proyestos:

     `cd~`

     `mkdir projects`

      `cd projects`

 3. Clona el repositorio con SSh

    `git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git`

Inicialmente, abre y lee la documetacion del API de "Urban Grocers".  Toda la documentacion necesaria se encuentra en el archivo Configuration. 
En el archivo Data se encuentra el diccionario para poder implementar las funciones necesarias en el archivo Sender_Stand_Request.
Se encuentran almacenadas las funciones de automatizacion de las solicitudes de las pruebas positivas y negativas en el archivo Create_kit_name_kit_test.

### Que podemos apreciar en los archivos:

#### _Configuration:_
* La URL del servidor. 
* El Endpoint para consultar la documentacion. 
* Los Endpoints para crear un nuevo usuario y un kit.

#### _Data:_ 
* El Heather del  aplicativo.
* El parametro de la variante **user_body** necesario para la creacion de un nuevo usuario con el conjunto minimo de datos. Como por ejemplo: nombre, numero telefonico y direccion, en formato JSON.
* El parametro de la variante **kit_body** en formato JSON
* Los nueves parametros de la variante **name** en formato Json. Con las que se realizaran las pruebas del archivo create_kit_name_test.

#### _Sender_stand_request:_ 
* La funcion **def** con el metodo **post** para crear un nuevo usuario. 

```
  def post_new_user(body): 
      return requests.post(configuration.URL_SERVICE +configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
```
  

* La funcion **def** con el metodo **get** para solicitar la autenticacion del "auth_token" del usuario, ya que es necesaria para la creacion del kit.
```
def get_user_token():
    user_token = post_new_user(data.user_body)
    user_json = user_token.json()
    auth_token = user_json['authToken']
    return auth_token
```
 
* La funcion **def** con el metodo **get** de crear un nuevo kit.
```
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
```


#### _Create_kit_name_kit:_
* En la prueba positiva de automatizacion de los kits utilizamos la funcion **def** con el metodo de comprobacion **positive_assert**. 
```
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert response.json()["name"] != ""
```

* En la prueba negativa de automatizacion de los kits utilizamos la funcion **def** con el metodo de comprobacion **negative_assert**. Con sus respectivos mensajes de error. 
```
def negative_assert_symbol(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body) 
    assert response.status_code == 400
	assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos. " \
                                      	  "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
```

* La lista de comprobacion positiva y negativa de los nueve kits, contiene la funcion **def** y el sufijo **test** para indicar que una prueba.
```
def test_create_1_character_new_kit_body_get_success_response():
    positive_assert(data.kit1)
    
def test_create_511_character_new_kit_body_get_success_response():
    positive_assert(data.kit2)

def test_create_0_character_new_kit_body_get_error_response():
    negative_assert_symbol(data.kit3)
    
def test_create_512_new_kit_body_error_response():
    negative_assert_symbol(data.kit4)
    
def test_create_special_character_new_kit_body_get_success_response():
    positive_assert(data.kit5)

def test_create_space_new_kit_body_get_success_response():
    positive_assert(data.kit6)
    
def test_create_number_new_kit_body_get_success_response():
    positive_assert(data.kit7)
    
def test_create_not_params_new_kit_body_get_error_response():
    negative_assert_symbol(data.kit8)
    
def test_create_number_new_kit_body_get_error_response():
    negative_assert_symbol(data.kit9)    
```

Para realizar la pruebas de automatizacion es necesario modificar el nombre de la prueba a manera explicatica del caso, usando el metodo snake.  Y la variable **(kit_body)** en el metodo **assert** que se encuentra en el archivo Data.

* Las pruebas positivas dieron un 100% de eficacia. De manera contraria sucede con las pruebas negativas,
ya que se han mostrado unos errores en los kits 3, 4, 8 y 9. Todas las pruebas han sido ejecutadas adicionalmente en Postman, dando error en algunas de ellas. Los respectivos errores se pueden observar en el siguiente informe:  [es un ejemplo de escenario](http:// no funciona "es una ejemplo de escenario")

La prueba 3 deberia de dar como resultado un error 400 pero el actual es un 201 creando el kit.
La prueba 4 deberia de dar como resultado un error 400 pero el actual es un 201 creando el kit.
La prueba 8 deberia de dar como resultado un error 400 pero el actual es un 500.
La prueba 9 deberia de dar como resultado un error 400 pero el actual es un 201 creando el kit.

![img_1.png](img_1.png)