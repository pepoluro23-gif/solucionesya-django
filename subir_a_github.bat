@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo  Subir proyecto a GitHub (commits por etapa)
echo ============================================
echo.
git --version >nul 2>&1 || (echo No se encontro Git instalado. & pause & exit /b)
if exist .git (echo Este proyecto ya tiene Git inicializado. Usa git add / commit / push normalmente. & pause & exit /b)

for /f "delims=" %%i in ('git config --global user.name') do set GNAME=%%i
if "%GNAME%"=="" (
    set /p GNAME=Tu nombre para Git: 
    call git config --global user.name "%%GNAME%%"
    set /p GMAIL=Tu email de GitHub: 
    call git config --global user.email "%%GMAIL%%"
)

set REPO=https://github.com/pepoluro23-gif/solucionesya-django.git

git init
git branch -M main

git add .gitignore .env.example requirements.txt manage.py config
git commit -m "Configuracion inicial del proyecto Django (settings, urls, dependencias)"

git add pages/__init__.py pages/apps.py pages/models.py pages/admin.py pages/migrations
git commit -m "Modelo Servicio (post del blog) con imagen y texto enriquecido, registrado en el admin"

git add templates/base.html static
git commit -m "Plantilla base con Bootstrap, navbar y herencia de templates"

git add pages/forms.py pages/views.py pages/urls.py templates/pages
git commit -m "CRUD de posts con vistas basadas en clases, buscador y rutas protegidas"

git add accounts templates/accounts
git commit -m "Usuarios: registro, login, logout, perfil con avatar y cambio de contrasena"

git add pages/tests.py pages/management
git commit -m "Tests y comando cargar_datos con posts de ejemplo"

git add .
git commit -m "README con instalacion y uso, script de inicio para Windows"

git remote add origin %REPO%
git push -u origin main

echo.
echo Listo. Repo: https://github.com/pepoluro23-gif/solucionesya-django
echo Pega esa URL en Coderhouse.
pause
