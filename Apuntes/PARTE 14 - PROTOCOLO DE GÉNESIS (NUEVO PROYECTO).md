🦾 SDET MASTER BIBLE: PARTE 14 - PROTOCOLO DE GÉNESIS (NUEVO PROYECTO)
Esta sección es la "Receta Maestra" para crear un framework desde cero en 5 minutos usando el ADN de tus proyectos anteriores.
🧬 1. EL ADN DEL PROYECTO (requirements.txt)
Este archivo es la "lista de la compra" que permite clonar tu taller en cualquier PC.
A. Cómo crear el ADN (En tu proyecto actual)
Cuando tu taller ya tiene todas las herramientas instaladas y funcionando:
Abre la terminal en la raíz.
Escribe: pip freeze > requirements.txt
Resultado: Se crea un archivo de texto con toda la "artillería" y sus versiones exactas.
B. Cómo inyectar el ADN (En un proyecto NUEVO)
Si empiezas de cero, no instales nada a mano:
Copia el archivo requirements.txt de tu proyecto viejo y pégalo en la carpeta del nuevo.
En la terminal del nuevo proyecto (con el .venv activo), escribe:
pip install -r requirements.txt
Resultado: Python instala TODO automáticamente.
📋 2. EL CHECKLIST "ZERO TO HERO" (Paso a paso real)
Si mañana tienes que automatizar una web nueva, sigue estos 8 pasos en este orden exacto:
CARPETA: Crea una carpeta con nombre profesional (ej: banco_pro_automation) y ábrela en VS Code.
BÚNKER (Entorno Virtual): Crea el aislamiento térmico:
code
Bash
python -m venv venv
LLAVE (Activar): Entra en la habitación:
code
Bash
.\venv\Scripts\activate
ADN (Librerías): Pega tu requirements.txt en la raíz y ejecuta:
code
Bash
pip install -r requirements.txt
OJOS (Navegadores): Descarga los motores de búsqueda:
code
Bash
playwright install
ESTRUCTURA: Crea las carpetas pages/ y tests/.
PAQUETE: Crea un archivo vacío llamado __init__.py dentro de la carpeta pages/.
BIOS (Configuración): Copia y pega los archivos pytest.ini y .gitignore de tu proyecto anterior.
🧠 3. ¿QUÉ SE REUTILIZA Y QUÉ SE CREA DE NUEVO?
Como Senior, no reescribes todo. Reutilizas la inteligencia, pero no el músculo.
✅ LO QUE TE LLEVAS (Copiar y Pegar):
Tu MASTER_STUDY_GUIDE.md (Tus apuntes).
El archivo requirements.txt (Para instalar rápido).
La estructura del pytest.ini (La configuración de velocidad).
La lógica del .gitignore (Para no subir basura a la nube).
El código del "Chivato de Fotos" del conftest.py (El hook de Allure).
❌ LO QUE NUNCA TE LLEVAS (Prohibido):
La carpeta .venv (Se debe crear una nueva en cada PC).
Las Pages (Cada web tiene sus propios botones).
Los Tests (Cada misión es distinta).
🧪 4. RESUMEN DE COMANDOS "FRANCOTIRADOR"
Acción	Comando
Guardar herramientas	pip freeze > requirements.txt
Instalar todo el ADN	pip install -r requirements.txt
Instalar navegadores	playwright install
Ver qué hay instalado	pip list
💡 5. LA ANALOGÍA DEL SENIOR (El Perfil de Impresión)
requirements.txt: Es el Perfil de Curado/Slicer. No configuras la temperatura, la velocidad y el soporte cada vez que imprimes. Guardas el perfil y se lo aplicas a la pieza nueva.
pip install -r: Es darle al botón de "Cargar Perfil". La impresora ya sabe exactamente cómo tiene que trabajar porque ha leído el archivo.