import requests
import pytest

@pytest.mark.parametrize("datos_a_enviar,nombre_esperado", [(
    {"name": "Salva", "email": "salvaceballosvelez@gmail.com", "username": "deagle94"}, "Salva"),
    ({"name": "Cristian", "email": "cristian_xulino@gmail.com", "username": "piru"}, "Cristian")])

def test_refuerzo_parametrizacion(datos_a_enviar, nombre_esperado):
    respuesta = requests.post("https://jsonplaceholder.typicode.com/users", json=datos_a_enviar)
    assert respuesta.status_code == 201
    datos = respuesta.json()
    assert datos["name"] == nombre_esperado
    assert datos["username"] == datos_a_enviar["username"]
    assert datos["email"] == datos_a_enviar["email"]