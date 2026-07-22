1. Entrar en la carpeta	                     cd playwright_python_pom
2. Activar el Búnker	                     .\.venv\Scripts\Activate.ps1
3. Lanzar Test con Navegador	             python -m pytest --alluredir=reporte_allure --clean-alluredir
4. Lanzar Test "Camuflado" (Rápido)	         python -m pytest --alluredir=reporte_allure --clean-alluredir --headless --slowmo 0
5. Abrir Reporte Allure	                     allure serve reporte_allure