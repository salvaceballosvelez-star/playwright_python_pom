⚔️ GUION DE SHOWROOM: INFRAESTRUCTURA & REPORTING
1. NAVEGACIÓN AL CAMPO DE BATALLA
Lo primero es entrar en la carpeta raíz. Si abres la terminal y no estás en el sitio, este es el comando maestro:
code
Powershell
cd "C:\Users\SalvadorCeballos\OneDrive - SEABERY\Escritorio\Curso Python\Curso Python\Proyectos\playwright_python_pom"
Qué decir: "Entro en la raíz del proyecto para asegurar que el Python Path reconoce el paquete de 'pages' y el archivo de configuración 'pytest.ini'."
2. ACTIVACIÓN DEL BÚNKER (ENTORNO VIRTUAL)
Si no ves el (.venv) al principio de la línea, activa el entorno:
code
Powershell
.\.venv\Scripts\Activate.ps1
Qué decir: "Activo el entorno virtual para garantizar que las dependencias de Playwright y Pytest están aisladas y no entran en conflicto con el Python global del sistema."
3. EJECUCIÓN DE ARTILLERÍA (TEST 09 - PARAMETRIZADO)
Vamos a lanzar el test de los 3 usuarios. Es el que más impresiona porque se repite solo.
code
Bash
python -m pytest tests/test_09_multi_usuarios.py -v --alluredir=reporte_allure
-v: Para que vea los nombres de los usuarios en la terminal.
--alluredir: Para que guarde los ingredientes del reporte.
Qué decir: "Voy a ejecutar una suite parametrizada. Fíjate cómo Pytest desacopla los datos del código, generando tres hilos de ejecución independientes para validar diferentes perfiles de usuario en un solo test."
4. EL GRAN FINAL: LEVANTAR EL DASHBOARD
Ahora es cuando sacas los gráficos de tarta:
code
Bash
allure serve reporte_allure
Qué decir: "Ahora levanto el servidor de Allure para procesar los artefactos JSON. Esto nos genera un dashboard ejecutivo con trazabilidad de steps, severidad y tiempos de respuesta de la red."
🚑 EL TRUCO DEL SENIOR (Si el navegador no se abre solo)
Si Allure dice "Generating report..." pero no se abre la web, no te pongas nervioso. Mira la terminal, busca el link que empieza por http://192.168... o http://127.0.0.1..., cópialo y pégalo tú mismo en Chrome.
Qué decir: "El hook de apertura automática está restringido por la política de grupo de la oficina, pero el servidor Jetty ya está arriba. Accedo manualmente a la instancia local."
🛡️ 3 FRASES PARA REMATAR LA REUNIÓN:
Sobre el POM: "He estructurado el proyecto bajo Page Object Model para que, si el equipo de desarrollo cambia un ID, solo tengamos que actualizar un único punto de entrada en la capa de 'pages'."
Sobre las Fixtures: "Uso inyección de dependencias en el conftest.py para gestionar el ciclo de vida del navegador, permitiendo que los tests se teletransporten a cualquier estado de la aplicación."
Sobre Allure: "Esta capa de reporting no solo es visual; nos permite adjuntar evidencias como screenshots o logs de red automáticamente cuando un test falla en el pipeline."