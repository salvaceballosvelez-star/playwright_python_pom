#Importar la libreira para poder llamar a la API
import requests

#Crear función empezando con test_ para que pytest lo reconozca como un test
def test_api_get_usuario():

#Crear variable para guardar la respuesta de la API y usar requests.get 
# para hacer la llamada a la API entre ("") siempre va la url
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/2")
#Comprobar la respuesta de la API con un assert para verificar que el status code sea 200
    assert respuesta.status_code == 200

#Extraer los datos de la respuesta en formato JSON y guardarlos en una variable
    datos = respuesta.json()
#Comprobar que el id del usuario sea 2 con un assert
    assert datos["id"] == 2
#Comprobar que el nombre del usuario sea "Ervin Howell" con un assert
    assert datos["name"] == "Ervin Howell"
    