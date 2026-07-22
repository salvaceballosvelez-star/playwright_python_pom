🦾 SDET MASTER BIBLE: PARTE 2 - EL ESPECIALISTA (PAGE OBJECT MODEL)

Esta sección explica cómo mapear una página web para que el código sea ordenado y fácil de arreglar.

🏛️ 1. LA CLASE (El Molde del Personaje)
Cada página de la web es una Clase. Imagínala como una ficha de personaje de tu RPG. La ficha dice qué objetos tiene el personaje y qué habilidades sabe usar.

Regla de Oro: 1 Página de la web = 1 Archivo .py en la carpeta /pages.

🛠️ 2. EL CONSTRUCTOR (__init__): EL INVENTARIO
Es lo primero que se ejecuta. Aquí es donde "pones las herramientas sobre la mesa".

    Misión: Identificar DÓNDE están los botones y cajas de texto.
    PROHIBIDO: Hacer clic o escribir aquí. Solo guardas las direcciones (Locators).

class LoginPage:
    def __init__(self, page: Page):
        # 1. EL BOLSILLO (self.page): Guardamos el navegador para usarlo luego.
        self.page = page 
        
        # 2. LAS PEGATINAS (Locators): Guardamos la ubicación de los elementos.
        # Usamos nombres en inglés y abreviaturas pro (_field, _btn).
        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_btn = page.locator("#login-button")

⚔️ 3. LOS MÉTODOS (Las Habilidades / Acciones)
Son las funciones (def) que ejecutan movimientos reales en la web.

    Misión: Decirle al robot QUÉ HACER con las herramientas del inventario.
    Regla de Salvador: Si el método está en AMARILLO en VS Code, es una acción y SIEMPRE LLEVA PARÉNTESIS ().

def enter_app(self, user, pwd):
        # Usamos las herramientas del inventario (self.)
        self.username_field.fill(user) # Escribir
        self.password_field.fill(pwd) # Escribir
        self.login_btn.click()        # Clicar (¡Con paréntesis!)


🧠 4. EL MISTERIO DEL self. (Explicación para tontos)
Muchos se rallen con el self. Piénsalo así:

    page (a secas): Es un navegador que pasa por la calle. Si no lo agarras, se va.
    self.page: Es el navegador que TÚ has agarrado y te has metido en el bolsillo. Ahora es tuyo y puedes usarlo en cualquier función de tu clase porque "te pertenece".
    Regla: Si quieres usar algo que definiste en el __init__, tienes que ponerle self. delante. Si no, la función no lo encontrará.

🏷️ 5. DICCIONARIO DE NOMBRES (Naming Conventions)
Para que tu código parezca el de un Senior de 45k€, usa siempre estos sufijos:

Elemento	            Sufijo	            Ejemplo
Botón:	                _btn	            submit_btn
Campo de texto:	        _field o _input	    user_field
Texto / Etiqueta:	    _txt o _lbl	        error_msg_txt
Icono / Imagen:	        _icon o _img	    cart_icon
Desplegable:	        _ddl o _select	    sort_ddl


 6. LA LEY DEL SILENCIO (Mudez de la Página)
Las Pages son MUDAS.

    Ellas no saben si el test está pasando o fallando.
    NUNCA pongas un expect() dentro de una Page.
    Si quieres comprobar algo, el método debe devolver el dato al test usando return.