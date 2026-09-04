#Importo el modulo de request para hacer peticiones http no pongo el pytest por que es solo 1 prueba y no necesito parametrizar
import requests

#Creo una funcion para poder hacer la prueba del put 
def test_put_usuario():
    #Creo una variable con la nueva informacion que quiero actualizar del usuario con id 2
    datos_actualizados = {"name": "Salva Actualizado", "username": "deagle94", "email": "salvaceballosvelez@gmail.com"}
    #Creo otra variable con la repuesta de la APi con los datos actualizados y hago un assert para que me devuelva el 200 por
    # la peticion de put que actualiza los datos del usuario con id 2
    respuesta = requests.put("https://jsonplaceholder.typicode.com/users/2", json=datos_actualizados)
    #Assert devuelve un 200 por que la peticion de put fue exitosa y actualizo los datos del usuario con id 2
    assert respuesta.status_code == 200
    ##Crea otra variable para comparar con otro assert y comprobar que el nombre del usuario con id 2 se actualizo correctamente
    datos = respuesta.json()
    #Assert devuelve la nueva informacion del usuario con id 2 y comprueba que el nombre se actualizo correctamente
    assert datos["name"] == "Salva Actualizado"