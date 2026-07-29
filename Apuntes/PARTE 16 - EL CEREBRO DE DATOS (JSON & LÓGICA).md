🦾 SDET MASTER BIBLE: PARTE 16 - EL CEREBRO DE DATOS (JSON & LÓGICA)
Esta sección es el manual para conectar archivos externos con tu código. Úsalo cuando no quieras escribir datos fijos en el test.
📦 1. LA ESTRUCTURA DEL JSON (El Búnker)
El archivo .json es una serie de cajas dentro de otras cajas.
code
JSON
{
  "login": {
    "user": "standard_user",
    "pass": "secret_sauce"
  },
  "compra": ["backpack", "onesie"]
}
Llaves { }: Son "Cajas con etiquetas". Para sacar algo, usas su nombre.
Corchetes [ ]: Son "Listas de objetos". Para sacarlos, usas un bucle for.
📖 2. CÓMO "BEBER" DEL ARCHIVO (El Código Sagrado)
Para leer el archivo desde tu test, usa siempre estas 3 líneas exactas:
code
Python
import json # 1. Traes el traductor al principio del archivo

# 2. Abres la caja. 'data.json' es el nombre del archivo.
# 'f' es el nombre temporal que le damos al archivo abierto.
with open("data.json") as f:
    # 3. Guardas todo el contenido en una variable llamada 'data'
    data = json.load(f)
📍 3. CÓMO LLEGAR AL DATO (El rastro de migas)
Una vez que tienes la variable data, llegas al fondo usando los nombres de las etiquetas entre corchetes:
Para el usuario: data["login"]["user"]
(Entra en la caja 'login' y coge la etiqueta 'user')
Para la lista de productos: data["compra"]
(Coge la lista entera para usarla en un for)
🚦 4. LA TOMA DE DECISIONES (if / ==)
Sirve para que el robot haga algo especial solo cuando se cumpla una condición.
Regla de Oro:
= (Un igual): Es para GUARDAR un dato. (nombre = "Salva")
== (Dos iguales): Es para COMPARAR. (¿Es nombre == "Salva"?)
code
Python
# Ejemplo: Sacar foto solo si el producto es la mochila
if item == "backpack":
    page.screenshot(path="mochila.png")
🏗️ 5. GUÍA DE MONTAJE PARA EL TEST (Paso a Paso)
Si tienes que hacer un test que use JSON, sigue este orden:
Importar: import json arriba del todo.
Cargar: Usa el bloque with open al principio de la función del test.
Extraer: Guarda el usuario y la contraseña en variables:
user = data["login"]["user"]
Actuar: Usa esas variables en el login.enter_app(user, password).
Bucle: Si hay una lista de productos, usa el for item in data["compra"]:.
Validar: Usa len(data["compra"]) para saber cuántos productos esperar en el carrito.
🛡️ NOTA PARA SALVADOR:
"Fiera, no intentes memorizar json.load(f). Intenta memorizar que el JSON es la tarjeta SD y el Python es la impresora. Cuando necesites el código, ven aquí, busca la Sección 2 y cópiala. Eso es lo que hacemos los Seniors."