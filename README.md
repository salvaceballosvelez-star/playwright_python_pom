# [Nombre del proyecto]

## ¿Qué es esto?
Este proyecto conciste en automatizar la pagina saucedemo para poder realizar testing automatico, el objtivo es encontrar problemas que se le puede dar a un cliente para que el DEV pueda corregirlo y dar una mejor exp de usuario.

## Stack técnico
(Python, Playwright, Pytest, Allure...)

## Arquitectura
Usamos el sistema POM, por que es un sistema de facil escalabilidad y entendimiento entre los QA automaticos, el POM permite que si en el futuro se tenga que cambiar pruebas sea mas facil el cambio sin tener que hacer grandes refactos.

## Cómo instalarlo
1 - Instalar pytest-playwright
2 - Instalar playwrigh
3 - Instalar todo lo del archivo requirement

## Cómo lanzar los tests
1. Entrar en la carpeta	                     cd playwright_python_pom
2. Activar el Búnker	                     .\.venv\Scripts\Activate.ps1
3. Lanzar Test con Navegador	             python -m pytest --alluredir=reporte_allure --clean-alluredir
4. Lanzar Test "Camuflado" (Rápido)	         python -m pytest --alluredir=reporte_allure --clean-alluredir --headless --slowmo 0
5. Abrir Reporte Allure	                     allure serve reporte_allure

## Cómo ver el reporte
(allure serve reporte_allure)