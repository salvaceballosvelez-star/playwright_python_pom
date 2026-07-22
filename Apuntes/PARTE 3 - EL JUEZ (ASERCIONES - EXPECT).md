🦾 SDET MASTER BIBLE: PARTE 3 - EL JUEZ (ASERCIONES / EXPECT)

Esta sección explica cómo comprobar que la realidad de la web coincide con lo que tú esperas.

⚖️ 1. EL JUEZ (expect)
En Playwright, el comando expect es el Dungeon Master. Es el único que tiene el poder de mirar la pantalla y decir: "Esto es correcto, seguimos" o "Esto es un error, paramos la partida".

Regla de Oro: Un test sin un expect al final no es un test, es solo un script que mueve el ratón.

🔍 2. DICCIONARIO DE VEREDICTOS (Comandos Pro)
Comando	                        Qué mira el Juez	                Uso Real
to_have_url("...")	            La dirección del navegador.         ¿Hemos cambiado de página?
to_be_visible()	                Si el objeto se ve en pantalla.	    ¿Ha aparecido el mensaje de error?
to_have_text("...")	            El texto EXACTO.	                ¿El precio es exactamente "$29.99"?
to_contain_text("...")	        Si el texto CONTIENE algo.	        ¿El error menciona la palabra "locked"?
to_have_count(N)	            Cuántos elementos hay.	            ¿Hay 3 productos en el carrito?


📏 3. LA LEY DE LA BARRA FINAL (URLs)
Playwright es un juez literal. Un solo carácter de diferencia y te mandará al rojo.

    🌍 Dominios raíz (.com, .es, .net): Siempre terminan con barra → https://www.saucedemo.com/
    📄 Archivos o subpáginas (.html): Nunca llevan barra al final → inventory.html

Truco de Senior: Si no estás seguro, para el test con page.pause(), copia la URL directamente de la barra de direcciones y pégala en tu código. El navegador nunca miente.

🎯 4. PRECISIÓN QUIRÚRGICA: have vs contain
No te ralles, es muy fácil:

    to_have_text: Es como una contraseña. Si falta un punto o hay un espacio de más, FALLA.
    to_contain_text: Es como buscar una pista. Si el mensaje es "Epic sadface: Username is required" y tú buscas "Username", el Juez dice OK.
    Consejo: Usa to_contain_text para mensajes largos para evitar fallar por un simple punto o coma.

🚫 5. ¿DÓNDE SE SIENTA EL JUEZ? (Ubicación)

En pages/: El Juez tiene PROHIBIDA la entrada. Las páginas solo ejecutan órdenes.
En tests/: Aquí es donde el Juez manda. El archivo de test es el que decide cuándo llamar al Juez para validar un paso.


💡 6. EL JUEZ NEGATIVO (not_)

A veces quieres comprobar que algo NO está (por ejemplo, que has borrado un producto).

    Sintaxis: expect(locator).not.to_be_visible()
    Traducción: "Espero que este objeto NO se vea".