@echo off
cd /d "%~dp0"
if not exist .env copy .env.example .env >nul
if not exist .venv (
    echo Creando entorno virtual...
    python -m venv .venv
    call .venv\Scripts\activate
    echo Instalando dependencias...
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py cargar_datos
) else (
    call .venv\Scripts\activate
    python manage.py migrate
)
start "" http://127.0.0.1:8000
python manage.py runserver
pause
