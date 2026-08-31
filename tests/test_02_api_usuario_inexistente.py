#Importar la libreira para poder llamar a la API
import requests

#Crear función empezando con test_ para que pytest lo reconozca como un test
def test_usuario_inexistente():

#Crear variable para guardar la respuesta de la API y usar requests.get 
# para hacer la llamada a la API entre ("") siempre va la url
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/999")
#Comprobar la respuesta de la API con un assert para verificar que el status code sea 404 por que el usuario es inexistente
    assert respuesta.status_code == 404

#Extraer los datos de la respuesta en formato JSON y guardarlos en una variable
    datos = respuesta.json()
#Comprobar que los datos sean un diccionario vacío con un assert
    assert datos == {}