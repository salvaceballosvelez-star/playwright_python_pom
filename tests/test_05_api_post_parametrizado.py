import requests
import pytest

@pytest.mark.parametrize("datos_a_enviar,nombre_esperado", [
    ({"name": "Juan", "username": "Juan_el_macho", "email": "El_juanito_17@gmail.com"}, "Juan"),
    ({"name": "Pepe", "username": "Pepito_top", "email": "pepito@gmail.com"}, "Pepe"),
])
def test_post_usuario_parametrizado(datos_a_enviar, nombre_esperado):
    respuesta = requests.post("https://jsonplaceholder.typicode.com/users", json=datos_a_enviar)
    assert respuesta.status_code == 201
    datos = respuesta.json()
    assert datos["name"] == nombre_esperado
    assert datos["username"] == datos_a_enviar["username"]
    assert datos["email"] == datos_a_enviar["email"]
