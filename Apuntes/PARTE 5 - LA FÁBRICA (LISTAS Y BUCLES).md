🦾 SDET MASTER BIBLE: PARTE 5 - LA FÁBRICA (LISTAS Y BUCLES)

Esta sección explica cómo dejar de clicar botones uno a uno y empezar a procesar grupos de elementos de un solo golpe.

📦 1. LA LISTA (El Inventario de la Misión)
Una lista es una caja donde guardas varios datos juntos. En QA la usamos para guardar nombres de productos, usuarios o códigos de error.

    Sintaxis: nombres = ["backpack", "onesie", "bike-light"]
    Regla: Los textos van entre comillas y separados por comas.

🔄 2. EL BUCLE for (La Cadena de Montaje)
El bucle sirve para repetir una acción por cada objeto que haya en una lista.

Explicación para tontos:
Imagina que tienes 10 camisetas y tienes que ponerles un sello.

    Manual: Coges camiseta 1 (sello), coges camiseta 2 (sello)... (Te cansas).
    Bucle for: "Por cada camiseta que haya en la caja, ponle un sello".

# for [nombre_temporal] in [lista_real]:
for item in compras:
    # Todo lo que esté aquí dentro (con espacio) se repetirá
    print(f"Procesando: {item}")

🏗️ 3. LAS REGLAS DE ORO DEL BUCLE (Evita el Error)

    Los Dos Puntos :: Siempre van al final de la línea del for. Si no los pones, el motor no arranca.

    El Sangrado (Indentación): Todo lo que quieras que se repita tiene que estar "empujado" a la derecha (4 espacios o un Tabulador). Lo que esté a la izquierda se ejecutará solo una vez al final.

    La Variable Temporal: El nombre que pongas después del for (ej: item) es el objeto que tienes en la mano en ese momento. Úsalo dentro del bucle.

🎣 4. EL COMANDO .all() (La Red de Pesca)

A veces no sabes los nombres de los botones, pero sabes que todos son iguales (ej: todos los botones de "Borrar" del carrito).

    Locator: self.all_btns = page.locator(".cart_button")
    Acción: lista_real = self.all_btns.all()
    Resultado: .all() convierte un locator que encuentra muchas cosas en una lista de Python que puedes recorrer con un for.


📍 5. ¿DÓNDE VA EL BUCLE? (Estrategia Senior)

Ubicación	            Para qué sirve	                                Ejemplo real
En la PAGE	            Para una acción física en una pantalla.	        "Clica en todos los botones de borrar".
En el TEST	            Para repetir una misión con datos distintos.	"Haz la compra con 3 usuarios diferentes".

🚀 6. EJEMPLO MAESTRO: EL BARRENDERO
Así se ve un método profesional que limpia el carrito sin importar si hay 1 o 100 productos:

def remove_all_items(self):
    # 1. Pescamos todos los botones de la pantalla
    botones = self.all_remove_btns.all()
    
    # 2. Los recorremos uno a uno
    for b in botones:
        # 3. Ejecutamos la acción (¡Con paréntesis!)
        b.click()


💡 7. EL TRUCO DEL CONTADOR (len)
Si quieres saber cuántas cosas hay en tu lista para decírselo al Juez:

    total = len(lista_de_compras)
    expect(badge).to_have_text(str(total))
