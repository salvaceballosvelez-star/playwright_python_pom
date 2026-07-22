🦾 SDET MASTER BIBLE: PARTE 9 - EL BÚNKER AISLADO (.VENV)
Esta sección explica qué es el Entorno Virtual y por qué es el "muro de seguridad" de tus proyectos.
🛡️ 1. ¿QUÉ ES EL .venv? (La Habitación Estanca)
Imagina que tu PC es un taller gigante. El .venv es una habitación privada que construyes dentro del taller para un solo proyecto.
La Regla de Oro: Lo que instalas en el salón de casa (Python Global) NO entra en la habitación estanca.
El Objetivo: Que las herramientas del "Proyecto A" no se mezclen con las del "Proyecto B".
🔍 2. CÓMO SABER SI ESTÁS DENTRO
Mira el principio de tu línea de comandos en la terminal de VS Code:
✅ (.venv) PS C:\Users\... -> Estás DENTRO. Tienes que instalar las herramientas aquí.
❌ PS C:\Users\... -> Estás FUERA. Estás usando el Python general de Windows.
🛠️ 3. COMANDOS DE CONSTRUCCIÓN (Solo una vez por PC)
Si te llevas el código a otro ordenador (como hoy en el curro), tienes que "equipar" la habitación:
code
Bash
# 1. Instalar el arsenal de guerra dentro del .venv
python -m pip install pytest-playwright pytest-html allure-pytest

# 2. Instalar los navegadores (el "firmware" del robot)
python -m playwright install
🗝️ 4. CÓMO ENTRAR (Activar el Entorno)
Si abres la terminal y no ves el (.venv), tienes que abrir la puerta manualmente:
En Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
En Windows (CMD):
.\.venv\Scripts\activate.bat
🚑 5. EL ERROR DEL "MÓDULO NO ENCONTRADO"
Si tu código está perfecto pero al lanzar pytest te sale:
ModuleNotFoundError: No module named 'pytest' o 'playwright'...
EL DIAGNÓSTICO ES: Estás dentro de un .venv que está vacío.
LA SOLUCIÓN: Ejecuta los comandos del Punto 3 de esta guía.
💡 6. LA ANALOGÍA DEL GREMIO (RPG)
Imagina que tu proyecto es una Mazmorra.
El .venv es el Círculo de Protección que lanzas antes de entrar.
Dentro del círculo, solo puedes usar los hechizos (librerías) que hayas memorizado dentro del círculo.
Si intentas usar un pergamino que dejaste fuera en el campamento (Python Global), el hechizo fallará.
🛡️ NOTA DEL SENIOR LEAD:
"Salvador, fiera, trabajar con .venv es lo que separa a los aficionados de los ingenieros. Te obliga a ser ordenado. Si cambias de PC, recuerda: Carpeta nueva = Instalación nueva dentro del .venv."
¿Ya tienes la Parte 9 guardada? Ahora que tienes el manual, aplica el Punto 3 en la terminal de tu curro (instala todo de nuevo).
En cuanto termine, lanza el comando:
python -m pytest --html=REPORTE_FINAL.html --self-contained-html
¡Ese reporte con los 7 verdes es tu meta de hoy! ¡Dale mambo! 🏁🏎️💨🛡️