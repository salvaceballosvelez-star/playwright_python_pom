import requests
import pytest

#Crear una funcion dodne esta el programa de prueba, el nombre de la funcion debe 
#empezar con test_ para que pytest lo reconozca como un test
def test_get_post_usuario():
    #Crear variable para guardar mi respuesta hacia la api y llamar a la api.
    respuesta = requests.post("https://jsonplaceholder.typicode.com/users", json = {"name": "Juan", "username": "Juan_el_macho", "email": "El_juanito_17@gmail.com"})
    #Comprobar la respuesta de la API con un assert para verificar que el status code sea 200
    assert respuesta.status_code == 201

    #Comprobar que el dicionario de datos de la respuesta contenga los datos que enviamos en el post
    datos = respuesta.json()
    #Compruenbo que el name, username y email sean los que enviamos en el post
    assert datos["name"] == "Juan"
    assert datos["username"] == "Juan_el_macho"
    assert datos["email"] == "El_juanito_17@gmail.com"

