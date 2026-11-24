# Soluciones Ya — Proyecto Final Python (Coderhouse)

Sitio web hecho con **Django** para **Soluciones Ya**, un emprendimiento de servicios a domicilio en
Viedma y Carmen de Patagones (armado de muebles, cámaras de seguridad, limpieza de tanques,
electricidad y plomería).

Es un **blog web**: cada **post** (modelo `Servicio`) muestra un servicio o un trabajo realizado, con
título, subtítulo, categoría, contenido con formato, imagen y fecha. Los usuarios registrados pueden
publicar, editar y borrar sus propios posts desde la interfaz web.

---

## Funcionalidades

| Requisito | Dónde está |
|---|---|
| Patrón MVT | Apps `pages` (publicaciones) y `accounts` (usuarios) |
| Herencia de plantillas | `templates/base.html`, que extienden todas las vistas |
| Home | `/` con las últimas 3 publicaciones |
| Acerca de mí | `/about/` |
| Listado de páginas con buscador | `/pages/`, busca por título, subtítulo o contenido y filtra por categoría |
| Mensaje cuando no hay datos | "No hay páginas aún" en el listado y en el home |
| Detalle de cada página | `/pages/<id>/` |
| CRUD completo con vistas basadas en clases | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| Mixins | `LoginRequiredMixin` y `EsAutorMixin` (solo el autor o un admin edita o borra) |
| Decorador | `@login_required` en `mis_servicios` y `editar_perfil` |
| Modelo con texto enriquecido, imagen y fecha | `Servicio`: título, subtítulo, categoría, contenido (CKEditor 5), imagen, fecha y autor |
| Registro, login y logout | `/accounts/signup/`, `/accounts/login/`, logout por POST |
| Perfil con avatar | `/accounts/profile/` y `/accounts/profile/editar/` (avatar, bio, teléfono, web, fecha de nacimiento) |
| Cambio de contraseña | `/accounts/profile/password/` |
| Admin de Django | `/admin/`, con los modelos `Servicio` y `Perfil` registrados |
| Tests | `pages/tests.py` y `accounts/tests.py` |

## Modelos

- **Servicio** (`pages`): `titulo`, `subtitulo`, `categoria`, `contenido` (texto enriquecido),
  `imagen`, `fecha`, `autor` (FK a User), `creado` y `actualizado`.
- **Perfil** (`accounts`): relación uno a uno con `User`, más `avatar`, `bio`, `telefono`, `web` y
  `fecha_nacimiento`. Se crea solo al registrar un usuario (señal `post_save`).

## Tecnologías

Python 3 · Django 6 · SQLite · Pillow · python-decouple · django-ckeditor-5 · Bootstrap 5 (incluido en
`static/vendor`, funciona sin internet)

## Cómo correrlo

> El repositorio **no incluye** `db.sqlite3` ni la carpeta `media/` (están en `.gitignore`), así que
> el proyecto arranca con una base limpia. Los pasos de abajo crean la base desde cero, y
> `cargar_datos` agrega posts de ejemplo para probarlo enseguida.

### Opción rápida (Windows)

Doble clic en `iniciar.bat`. La primera vez crea el entorno virtual, instala las dependencias, crea la
base de datos con datos de ejemplo y levanta el servidor en http://127.0.0.1:8000

### Opción manual

```bash
git clone https://github.com/pepoluro23-gif/solucionesya-django.git
cd solucionesya-django
python -m venv .venv
.venv\Scripts\activate          # en Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env          # en Mac/Linux: cp .env.example .env  (opcional: sin .env usa valores de desarrollo)
python manage.py migrate
python manage.py cargar_datos   # opcional: usuario demo y 4 publicaciones de ejemplo
python manage.py createsuperuser   # para entrar al panel /admin/
python manage.py runserver
```

Abrí http://127.0.0.1:8000

**Usuario de prueba** (después de `cargar_datos`): `demo` / `demo12345`

### Tests

```bash
python manage.py test
```

## Variables de entorno

La configuración sensible se lee con `python-decouple` desde un archivo `.env` que **no se sube** al
repositorio. En `.env.example` están las variables necesarias, sin valores reales:

| Variable | Para qué sirve |
|---|---|
| `SECRET_KEY` | Clave secreta de Django |
| `DEBUG` | `True` en desarrollo |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por coma |

Si no existe `.env`, el proyecto usa valores por defecto pensados solo para desarrollo local.

## Estructura

```
solucionesya-django/
├── config/          # settings y urls del proyecto
├── pages/           # app de publicaciones: modelo, vistas CRUD, buscador, tests
│   └── management/commands/cargar_datos.py
├── accounts/        # app de usuarios: registro, login, perfil, avatar
├── templates/       # base.html, pages/ y accounts/
├── static/          # css propio y Bootstrap
├── .env.example
├── iniciar.bat         # instala y levanta el servidor (Windows)
├── subir_a_github.bat  # primer push en commits por etapa
├── requirements.txt
└── manage.py
```

## Autor

**Dante Dirazar** · Viedma, Río Negro, Argentina
[LinkedIn](https://www.linkedin.com/in/dante-dirazar-6a0183274) · Curso de Python, Coderhouse (2026)
