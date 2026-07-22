🦾 SDET MASTER BIBLE: PARTE 11 - INTELIGENCIA DE REPORTE (ALLURE)
Esta sección explica cómo ponerle "etiquetas" y "capítulos" a tus tests para que el informe final sea una herramienta de decisión para el negocio.
🏷️ 1. LOS DECORADORES (Los "Sombreros" @)
En Python, las líneas que empiezan por @ son etiquetas que le dan superpoderes a la función que tienen justo debajo. En Allure las usamos para clasificar.
@allure.title("Nombre Épico"): Cambia el nombre técnico (test_login_01) por uno humano en el reporte.
@allure.description("Texto largo"): Explica qué hace el test sin que el jefe tenga que leer el código.
🔴 2. NIVELES DE SEVERIDAD (allure.severity)
Sirve para que el equipo sepa qué arreglar primero cuando hay muchos fallos.
Nivel	Cuándo usarlo (Criterio QA Lead)	Impacto
BLOCKER	La web no carga o el botón de pago no existe.	🛑 Parada total.
CRITICAL	El Login falla o el carrito no añade productos.	🔥 Funcionalidad clave rota.
NORMAL	Un mensaje de error tiene una errata o un filtro falla.	⚠️ Importante pero usable.
MINOR	Un icono está un poco movido o un color no es el exacto.	🩹 Fallo estético.
TRIVIAL	Una falta de ortografía en el pie de página.	🔍 Casi invisible.
📂 3. LOS PASOS (with allure.step)
Sirve para dividir el test en "capítulos" legibles. Se usa con la palabra with.
¿Por qué usar with?
Porque el with crea un "nido" (un espacio a la derecha). Todo lo que metas dentro de ese nido aparecerá agrupado en el reporte

with allure.step("Fase 1: Introducir datos"):
    # El robot hace las acciones...
    login.enter_app("user", "pass")

with allure.step("Fase 2: Validar resultado"):
    # El Juez dicta sentencia...
    expect(page).to_have_url("...")

🧪 4. LA PARAMETRIZACIÓN (@pytest.mark.parametrize)
Es el truco para evitar el "Copia-Pega". Permite ejecutar el mismo test con diferentes datos.
Sintaxis: @pytest.mark.parametrize("nombre_variable", ["dato1", "dato2"])
Uso: Probar 10 usuarios distintos, 5 tarjetas de crédito o 3 idiomas con un solo test.
💡 5. REGLAS DE ORO PARA EL REPORTE
Acción vs Verificación: Intenta tener siempre al menos dos with allure.step: uno para lo que el robot HACE y otro para lo que el Juez COMPRUEBA.
Variables en el título: Puedes usar la f para que el paso diga el nombre del dato real:
with allure.step(f"Buscando el producto: {nombre_item}"):
Severidad Realista: No pongas todo como CRITICAL. Si todo es crítico, nada es crítico. Usa tu criterio de QA 