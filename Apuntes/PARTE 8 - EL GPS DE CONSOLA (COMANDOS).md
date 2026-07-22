🦾 SDET MASTER BIBLE: PARTE 8 - EL GPS DE CONSOLA (COMANDOS)
Esta sección explica cómo manejar el terminal de VS Code. La consola es el mando de tu Anycubic: si no sabes los comandos, la impresora no se mueve.

🎯 1. MODO FRANCOTIRADOR (Ejecución Selectiva)
No siempre quieres lanzar todos los tests. A veces solo quieres recalibrar uno.

Objetivo	                Comando	                                            Explicación para Salvador
Lanzar TODO	                python -m pytest	                                Ejecuta todas las misiones de la carpeta /tests.
Un solo archivo	            python -m pytest tests/test_login.py	            Dispara solo a ese archivo concreto.
Por palabra clave	        python -m pytest -k "comprar"	                    Ejecuta cualquier test que tenga "comprar" en el nombre.
Solo los fallidos	        python -m pytest --lf	                            (Last Failed) Repite solo los que fallaron antes.

🕵️‍♂️ 2. MODO RAYOS X (Depuración y Visibilidad)
Cuando el test falla y no sabes por qué, necesitas ver las entrañas.

    -s (Speak): Deja que el robot hable. Muestra tus mensajes de print() en la terminal.
    -v (Verbose): Modo detallado. Te dice el nombre de cada test y el porcentaje de progreso.
    --headed: Abre el navegador. Sin esto, Pytest trabaja en "modo fantasma" (invisible).
    --slowmo 1000: Cámara lenta. Espera 1 segundo entre cada paso para que tus ojos lo sigan.

Comando Pro de Debugging:
python -m pytest tests/mi_test.py -s -v --headed --slowmo 500

🚀 3. EL TURBO DEL RYZEN 9 (Paralelismo)
Tienes 12 núcleos y 64GB de RAM. Sería un pecado lanzar los tests uno a uno.

    Instalación: pip install pytest-xdist
    Comando: python -m pytest -n auto
    Qué hace: Abre tantos navegadores como núcleos tenga tu procesador y ejecuta todos los tests a la vez. Esto es lo que te da el sueldo de 45k.

🚑 4. KIT DE PRIMEROS AUXILIOS (Errores Comunes)
A. "ModuleNotFoundError: No module named 'pages'"

    Causa: Estás intentando ejecutar el test desde dentro de la carpeta /tests.
    Solución: Escribe cd .. para volver a la raíz. Ejecuta siempre desde playwright_python_pom.

B. "collected 0 items"
    Causa 1: No has guardado el archivo (CTRL + S).
    Causa 2: El archivo o la función no empiezan por la palabra test_.

C. "TargetClosedError"
    Causa: El navegador se ha cerrado mientras Playwright buscaba un botón.
    Solución: Revisa los guiones (- vs _) en tus selectores. El robot se ha quedado esperando a algo que no existe.

🛠️ 5. MANTENIMIENTO DEL ENTORNO
Si cambias de PC o algo se rompe, ejecuta esto en orden:

    pip install playwright pytest-playwright pytest-html allure-pytest
    playwright install (Si este no funciona usa el de abajo)
    python -m playwright install

🏁 FIN DEL GRIMORIO - NIVEL 1

🛡️ ÚLTIMA REFLEXIÓN DEL SENIOR LEAD:
"Salvador, fiera, ya tienes el mapa completo. No intentes memorizarlo. Úsalo como un mecánico usa su caja de herramientas. Si te pierdes, vuelve al Punto 6 (Fixtures) o al Punto 4 (Selectores). La lógica ya la tienes, el resto es solo práctica."
