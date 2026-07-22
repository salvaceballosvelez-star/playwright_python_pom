🦾 SDET MASTER BIBLE: PARTE 12 - MANTENIMIENTO Y OBSERVABILIDAD
Esta sección explica cómo hacer que tu proyecto sea portátil y cómo hacer que el robot explique qué está haciendo en cada segundo.
📋 1. EL ARCHIVO requirements.txt (La Ficha Técnica)
Es la "lista de la compra" de tu proyecto. Sirve para que otro programador (o un servidor en la nube) instale todo tu taller con un solo comando.
Generar el archivo (Congelar):
pip freeze > requirements.txt
Instalar todo desde el archivo:
pip install -r requirements.txt
Regla de Oro: Ejecuta el "congelado" cada vez que instales una librería nueva para que tu lista siempre esté actualizada.
🕵️‍♂️ 2. LOGGING VS PRINT (La Caja Negra)
En el mundo profesional NO usamos print(). Usamos la librería logging.
Característica	print()	logging
Marca de tiempo	No (tienes que ponerla tú).	SÍ (sale la hora exacta del clic).
Niveles de gravedad	No. Todo es igual.	SÍ (INFO, WARNING, ERROR).
Destino	Solo la terminal.	Consola, archivos .log y reportes.
🛠️ 3. CONFIGURACIÓN DEL LOGGER (En conftest.py)
Para que el robot empiece a hablar con propiedad, ponemos este "cerebro" en el Mayordomo:
code
Python
import logging

# Configuración básica: Hora - Nivel de importancia - Mensaje
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)
🚦 4. LOS NIVELES DE ALERTA (Jerarquía)
Como QA Lead, tú decides qué importancia tiene cada mensaje:
logger.debug(): Detalles técnicos muy profundos (solo para programadores).
logger.info(): El estándar. "Login exitoso", "Producto añadido".
logger.warning(): "La web tarda en cargar, pero sigo adelante".
logger.error(): "No he encontrado el botón de pagar, el test va a morir".
🧪 5. USO EN LOS TESTS
Para usarlo en un test, tienes que "llamar al chivato" al principio del archivo:
code
Python
import logging
logger = logging.getLogger(__name__)

def test_ejemplo(page):
    logger.info("🚀 Iniciando la misión de prueba...")
    # ... código ...
    logger.info("✅ Paso completado con éxito.")
💡 6. LA ANALOGÍA DEL SENIOR (El Vuelo del Avión)
print(): Es como si el piloto saca la cabeza por la ventana y grita: "¡Estamos volando!". Nadie lo oye fuera del avión.
logging: Es la Caja Negra. Registra la altitud, la velocidad y cada botón que se pulsa con la hora exacta. Si el avión se estrella (el test falla), la Caja Negra te dice exactamente qué pasó un segundo antes del impacto.
