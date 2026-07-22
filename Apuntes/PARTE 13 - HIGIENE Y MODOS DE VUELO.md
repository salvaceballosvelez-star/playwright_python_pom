🦾 SDET MASTER BIBLE: PARTE 13 - HIGIENE Y MODOS DE VUELO
Esta sección explica cómo mantener el taller limpio y cómo cambiar entre el modo "Showroom" (para humanos) y el modo "Ninja" (para servidores).
🧹 1. LA REGLA DE LA RAÍZ (Project Root)
En el mundo Senior, el orden de las carpetas es sagrado.
Apertura Correcta: En VS Code, dale a File > Open Folder y elige únicamente la carpeta playwright_python_pom.
El Error de Diógenes: Nunca abras una carpeta que contenga varios proyectos a la vez. VS Code se vuelve loco con los intérpretes y las rutas.
👻 2. HEADLESS VS HEADED (Modos de Navegador)
Playwright tiene dos formas de ejecutar el motor:
Modo HEADED (Con Ventana):
Uso: Para programar, debugear y enseñar el trabajo a los jefes.
Comando: --headed en el pytest.ini.
Modo HEADLESS (Invisible / Ninja):
Uso: Para ejecuciones masivas, rapidez total y servidores en la nube (CI/CD).
Ventaja: Ahorra memoria RAM y procesador al no tener que "dibujar" la web en el monitor.
Dato Pro: Es el modo por defecto de Playwright. Si no dices nada, el robot es invisible.
⚙️ 3. LIMPIEZA DE LA BIOS (pytest.ini)
El archivo .ini no admite comentarios sucios con # al final de las líneas. Tiene que ser código puro.
Configuración Profesional Limpia:
code
Ini
[pytest]
# addopts: Opciones automáticas
# --slowmo 500: Retraso para que el ojo humano lo siga
# --browser chromium: El motor que vamos a usar
addopts = --slowmo 500 --browser chromium
testpaths = tests
🗑️ 4. ELIMINACIÓN DE "ZOMBIES" (Mantenimiento)
Para que el proyecto sea portable (como el de José), hay cosas que NUNCA deben viajar de un PC a otro:
.venv: El entorno virtual se crea de cero en cada PC. Nunca se copia y pega.
__pycache__: Basura temporal de Python. Se puede borrar sin miedo.
.pytest_cache: Memoria de Pytest. Se puede borrar sin miedo.
reporte_allure: Resultados viejos. Bórralos antes de una gran prueba para no contaminar el informe nuevo.
🚑 5. EL RESET MAESTRO (Si nada funciona)
Si el entorno se vuelve loco (rayas amarillas, errores de ruta), aplica el "Protocolo Salvador":
Borra la carpeta .venv.
Crea una nueva: python -m venv venv.
Activa: .\venv\Scripts\activate.
Instala: pip install -r requirements.txt.
Selecciona Intérprete: Ctrl + Shift + P > Python: Select Interpreter.
💡 6. LA ANALOGÍA DEL SENIOR (El Taller de F1)
Tu código (.py): Es el diseño del coche y el motor. Se puede llevar a cualquier circuito.
El entorno (.venv): Son los neumáticos y la gasolina. Se ponen nuevos en cada carrera (en cada PC) porque se degradan y dependen del asfalto (el Sistema Operativo).
El modo Headless: Es el túnel de viento. No necesitas ver el coche correr, solo necesitas los datos de telemetría para saber que es aerodinámico.

🏷️ 7. NOMENCLATURA DEL PROYECTO (Naming)
No todos los proyectos se llaman igual. El nombre es libre, pero un Senior sigue estas reglas para no parecer un novato:
Regla de Oro: Usa siempre snake_case (minúsculas y guiones bajos). Nunca uses espacios ni mayúsculas en el nombre de la carpeta raíz.
Estructura del nombre: [NombreDeLaApp]_[Herramienta]_[Patron]
Ejemplo para un banco: bank_playwright_pom
Ejemplo para un e-commerce: amazon_automation_framework
Ejemplo para una API: crm_api_testing
¿Por qué pusimos playwright_python_pom?
Porque estamos en fase de aprendizaje y queríamos dejar claro el Stack (Playwright + Python) y el Patrón (POM). En tu empresa, probablemente el proyecto de José se llame algo como qa-automation-core o testing-simulador.
🎮 La Analogía del Gremio (RPG)
Imagina que estás creando una nueva expansión.
No todas se llaman "Expansión 1".
Una se llamará "LA LLAMADA DEL GREMIO" y otra "EL DESPERTAR DEL TYRANT".
El nombre de la carpeta es el título de la caja, pero lo que hay dentro (las reglas de Pytest y las fichas de las Pages) siempre sigue la misma estructura.

