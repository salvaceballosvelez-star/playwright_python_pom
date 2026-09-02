#Importamos requests para llamar a la API y pytest para realizar las pruebas unitarias
import requests
import pytest
#Parametrizacion de los datos requequidos para el post, el titulo esperado y el cuerpo esperado
@pytest.mark.parametrize("datos_post,titulos_esperado,cuerpo_esperado", [
    ({"title": "mi primer post", "body": "Contenido del primer post"}, "mi primer post", "Contenido del primer post"),])

#Funcion para ejecutar el programa con los datos previamente parametrizados, 
#el nombre de la funcion debe empezar con test_ para que pytest lo reconozca como un test
def test_post_parametrizado(datos_post, titulos_esperado, cuerpo_esperado):
    #Se proporciona lso datos a la API para que cree un nuevo post y se verifica que el status code sea 201
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = datos_post)
    #Comparar el dato que se envio en el post con el que se recibe en la respuesta de la API,
    #se verifica que el status code sea 201 y que el titulo y el cuerpo sean
    assert response.status_code == 201
    #Se crea una variable para guardar la respuesta de la API pra poder usar el assert y verificar que 
    # el titulo y el cuerpo sean los esperados
    datos = response.json()
    #Se comparan los datos que se enviaron en el post con los que se recibieron en la respuesta de la API
    assert datos["title"] == titulos_esperado
    assert datos["body"] == cuerpo_esperado