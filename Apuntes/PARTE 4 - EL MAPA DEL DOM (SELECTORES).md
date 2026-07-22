🦾 SDET MASTER BIBLE: PARTE 4 - EL MAPA DEL DOM (SELECTORES)

Esta sección explica cómo encontrar los elementos en la selva del HTML. Si el selector está mal, el robot está ciego.

🛡️ 1. LA JERARQUÍA DE SUPERVIVENCIA (Criterio Senior)
    No todos los selectores valen lo mismo. Usa este orden de prioridad para que tus tests no se rompan cada vez que el diseñador cambie un color:

👑 EL REY: data-test / data-testid
    Por qué: Son atributos creados específicamente para nosotros (QA). No cambian nunca.
    Sintaxis: page.locator("[data-test='valor']")

🤴 EL PRÍNCIPE: id
    Por qué: Es único en toda la página. Es muy rápido.
    Sintaxis: page.locator("#id-del-boton") (Usa siempre la almohadilla #).

🧔 EL CABALLERO: Role o Text
    Por qué: Es lo que ve el usuario. Si el texto cambia, el test debe fallar porque el usuario se perdería.
    Sintaxis: page.get_by_role("button", name="Login")

👲 EL PUEBLO: class
    Por qué: Es inestable. Es pura "pintura" CSS. Si el botón pasa de azul a verde, la clase cambia y tu test muere.
    Sintaxis: page.locator(".clase_boton") (Usa siempre el punto .).

🎨 2. LA GRAMÁTICA DE LOS SÍMBOLOS

Para que no te ralles:

    # (Almohadilla) = Busca un ID.
    . (Punto) = Busca una CLASE.
    [] (Corchetes) = Busca un ATRIBUTO cualquiera.
    "" vs '' = Usa comillas dobles fuera y simples dentro para los atributos.
        Bien: "[data-test='username']"

⚠️ 3. LA TRAMPA DEL ESPACIO (Múltiples Clases)

Este es el error que más te ha costado esta semana.

En el HTML: class="btn btn_primary cart_button" (Los espacios separan nombres).

En tu código: Si quieres usar esas clases, TIENES QUE QUITAR LOS ESPACIOS y poner puntos.
    Mal: page.locator(".btn btn_primary") -> Playwright busca un elemento dentro de otro.
    Bien: page.locator(".btn.btn_primary.cart_button") -> Playwright busca un elemento que tenga las 3 etiquetas a la vez.

🚀 4. SELECTORES DINÁMICOS (F-Strings)
Cuando el nombre del botón cambia según el producto (mochila, gorra, etc.), usamos la f mágica.

producto = "backpack"
# Las llaves {} son el hueco donde se mete la variable
selector = f"[data-test='add-to-cart-sauce-labs-{producto}']"

🔍 5. HERRAMIENTAS DE EXPLORACIÓN (Rayos X)

    F12 (Inspector): Tu mejor amigo. Usa la flechita para pinchar en el botón y ver su "DNI" (sus atributos).
    Ctrl + F (En el Inspector): Escribe tu selector ahí. Si sale 1 of 1, es perfecto. Si sale 1 of 50, tu selector es demasiado genérico y el robot se confundirá.
    page.pause(): El botón de pánico. El test se para y te abre el Playwright Inspector para que pruebes selectores en vivo.


💡 6. EL TRUCO DEL "CONTENIDO" (:has-text)
Si no hay IDs ni data-tests, puedes buscar por lo que hay dentro:

    page.locator("button:has-text('Finish')")
    Traducción: "Busca un botón que tenga el texto Finish dentro".