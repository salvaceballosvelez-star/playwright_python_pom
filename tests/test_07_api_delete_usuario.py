#Importo la librería requests para poder hacer la petición DELETE a la API
import requests

#Funcion que crear una variable llamada repuesta y que introduce la orden que la respuesta va a ejecutar 
# en este caso la orden DELETE a la API para eliminar 
# el usuario con id 2. 
# Luego se hace una aserción para comprobar que el código de estado de la respuesta es 204, lo que indica que la eliminación fue exitosa.
def test_delete_usuario():
    respuesta = requests.delete("https://jsonplaceholder.typicode.com/users/2")
    assert respuesta.status_code == 204
