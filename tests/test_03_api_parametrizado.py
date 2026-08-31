#Importamos requests para llamar a la API y pytest para realizar las pruebas unitarias
import requests
import pytest

# Parametrizamos la prueba para que se ejecute con diferentes valores de usuario_id y status_esperado
@pytest.mark.parametrize("usuario_id,status_esperado,json_esperado",[
    (2,200,{"id": 2, "name": "Ervin Howell", "username": "Antonette", "email": "Shanna@melissa.tv"}),(999,404, {}),
    ])

def test_get_usuario(usuario_id,status_esperado, json_esperado):
    # Se llama a la API con el ID de usuario proporcionado
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{usuario_id}")
    # Se verifica que el código de estado de la respuesta sea el esperado
    assert response.status_code == status_esperado

    if json_esperado == {}:
        # Si el diccionario de datos esperados está vacío, se verifica que la respuesta JSON también esté vacía
        assert response.json() == {}

#Se verifica que el contenido de la respuesta sea el esperado ya que en la parametrizacion el 3er 
# Puesto es el dicionario de los datos esperados
    for clave in json_esperado:
        # Se verifica que el valor de cada clave en la respuesta JSON sea igual al 
        # valor esperado en el diccionario json_esperado
        assert response.json()[clave] == json_esperado[clave]


