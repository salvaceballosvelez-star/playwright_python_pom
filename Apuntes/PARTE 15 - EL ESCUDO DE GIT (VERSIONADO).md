🦾 SDET MASTER BIBLE: PARTE 15 - EL ESCUDO DE GIT (VERSIONADO)
Copia esto en tus apuntes antes de empezar la acción.
🛡️ 1. ¿QUÉ ES GIT Y GITHUB?
Git: Es el programa que instalas en tu PC. Es como el sistema de "Historial de versiones" de tu Anycubic. Si una pieza sale mal, puedes volver a la configuración de ayer.
GitHub: Es la nube donde guardas ese historial. Es tu escaparate para el mundo y tu herramienta de sincronización.
🚫 2. LA REGLA SAGRADA DEL .gitignore
Nunca, jamás, se sube el "músculo" (.venv) ni la "basura" (__pycache__). Solo subimos el "cerebro" (el código). Tu archivo .gitignore ya está configurado para esto. ✅
🚀 PASO A PASO: TU PRIMER REPOSITORIO (En la ofi)
Sigue estos pasos en la terminal de VS Code. Si uno falla, no sigas.
PASO 1: Comprobar si tienes Git
Escribe: git --version
Si te sale un número (ej: git version 2.45.0), vamos bien.
Si te sale error, escribe: scoop install git y reinicia VS Code.
PASO 2: Inicializar el Taller Local
Dile a la carpeta que ahora es un proyecto de Git:
code
Bash
git init
PASO 3: El Primer "Commit" (Foto del estado actual)
Vamos a guardar el estado de tu proyecto hoy.
code
Bash
# 1. Seleccionamos todo (Git ignorará lo del .gitignore solo)
git add .

# 2. Guardamos con un mensaje profesional
git commit -m "feat: initial framework structure with POM and Pytest fixtures"
PASO 4: Crear el búnker en la nube (GitHub)
Abre GitHub.com en el navegador.
Dale al botón "+" (arriba a la derecha) > New repository.
Nombre: playwright_python_pom.
IMPORTANTE: Déjalo en Public (para tu portfolio) y NO marques nada de "Add a README" o ".gitignore" (ya los tenemos nosotros).
Dale a Create repository.
PASO 5: Conectar tu PC con la Nube
GitHub te enseñará unas líneas de código. Busca la que dice "…or push an existing repository from the command line". Copia y pega esas 3 líneas en tu terminal:
code
Bash
git remote add origin https://github.com/TU_USUARIO/playwright_python_pom.git
git branch -M main
git push -u origin main


# 🦾 SDET MASTER BIBLE: PARTE 15 - EL ESCUDO DE GIT (VERSIONADO)
*Esta sección explica cómo mover tu código entre la oficina y casa sin romper nada.*

## 🚀 1. COMANDOS DE TRABAJO DIARIO (El Ciclo de Vida)
Cada vez que termines una hora de práctica, haz esto para guardar tu progreso:

1. `git add .` (Mete todos los cambios en la maleta).
2. `git commit -m "mensaje descriptivo"` (Cierra la maleta y le pone una etiqueta).
3. `git push` (Envía la maleta a la nube de GitHub).

## 📥 2. CÓMO RECUPERAR EL CÓDIGO EN OTRO PC
Si llegas a casa y quieres lo que hiciste en la ofi:
*   **La primera vez:** `git clone https://github.com/tu_usuario/tu_repo.git`
*   **Las siguientes veces:** `git pull` (Baja los cambios nuevos de la nube).

## 🚫 3. LA REGLA DE ORO DEL .gitignore
Nunca subas la carpeta `.venv`. Cada PC debe tener la suya propia. Git la ignorará automáticamente gracias al archivo `.gitignore` que creamos.