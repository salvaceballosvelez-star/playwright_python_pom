🦾 SDET MASTER BIBLE: PARTE 7 - EL SHOW VISUAL (REPORTING)
Esta sección explica cómo generar evidencias físicas y reportes profesionales para que no tengas que explicar tus tests con palabras.

📸 1. LA CÁMARA DE FOTOS (.screenshot)
Playwright puede sacar fotos en cualquier momento. Es tu "Caja Negra".

    Foto de toda la web: page.screenshot(path="nombre.png")
    Foto de un solo objeto: self.boton.screenshot(path="solo_boton.png")
    Foto de página completa (con scroll): page.screenshot(path="largo.png", full_page=True)

📊 2. EL ACTA DE GUERRA (pytest-html)
Es un reporte sencillo en una página web que se genera al terminar los tests.

    Comando para generarlo:
    python -m pytest --html=REPORTE.html --self-contained-html
    Uso: Es el archivo que le envías por Slack a tu compañero para decirle "Todo está en verde".

🏆 3. EL DASHBOARD PRO (ALLURE)
Es el reporte de nivel Senior (el de los gráficos de tarta y emojis). Para que luzca, usamos Decoradores (etiquetas con @).

Decorador	                            Para qué sirve	                Ejemplo
@allure.title	                        Nombre épico del test.	        @allure.title("Compra de Mochila")
@allure.severity	                    Prioridad del test.	            severity_level.CRITICAL
with allure.step	                    Divide el test en pasos.	    with allure.step("Paso 1: Login")

🚨 4. EL "CHIVATO" (Screenshots automáticos)
Un Senior no saca fotos de todos los tests (gastaría mucha memoria). Un Senior programa un "sensor de colisión" en el conftest.py.
Lógica del Chivato:

El robot vigila el test.

    SI EL TEST PASA: No hace nada.
    SI EL TEST FALLA: Saca una foto en el milisegundo exacto del error y la pega en el reporte.
(Este código te lo daré masticado para que lo pegues en tu conftest, no hace falta memorizarlo)

🛠️ 5. INSTALACIÓN DE ARTILLERÍA
Si cambias de ordenador o el Ryzen 9 se formatea, necesitas estos comandos:

    pip install pytest-html (Reporte básico).
    pip install allure-pytest (Reporte Pro).

🔍 6. CÓMO LEER UN REPORTE (Criterio QA Lead)
Cuando abras el HTML, no mires solo el color verde. Mira:

    Duration: Si un test de login tarda 30 segundos, algo va mal en el servidor.
    Logs: Haz clic en el test para ver tus mensajes de print (usa el comando -s para que salgan).
    Errors: Si hay una F roja, lee la última línea; ahí está el "cadáver" del error.