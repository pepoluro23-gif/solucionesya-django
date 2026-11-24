from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from pages.models import Servicio

DATOS = [
    ('Armado de placard de 6 puertas', 'Placard melamina 1,80 m en Viedma centro', 'muebles',
     '<p>Armado completo de placard de <strong>6 puertas y 3 cajones</strong>, nivelado y fijado a la pared.</p>'
     '<ul><li>Tiempo: 4 horas</li><li>Incluye regulación de bisagras</li></ul>', date(2026, 10, 2)),
    ('Kit de 4 cámaras de seguridad', 'Instalación con DVR y acceso desde el celular', 'camaras',
     '<p>Instalación de <strong>4 cámaras Full HD</strong> con grabador DVR, cableado embutido '
     'y configuración de la app para ver en vivo desde el celular.</p>', date(2026, 10, 15)),
    ('Limpieza de tanque de 1.000 litros', 'Vaciado, cepillado y desinfección', 'tanques',
     '<p>Limpieza integral de tanque de agua: vaciado, cepillado de paredes, '
     'desinfección con cloro y enjuague.</p><p><em>Recomendado cada 6 meses.</em></p>', date(2026, 11, 1)),
    ('Cambio de tablero eléctrico', 'Térmicas y disyuntor diferencial nuevos', 'electricidad',
     '<p>Reemplazo de tablero viejo por uno nuevo con <strong>disyuntor diferencial</strong> '
     'y llaves térmicas por circuito.</p>', date(2026, 11, 10)),
]


class Command(BaseCommand):
    help = 'Crea un usuario demo y publicaciones de ejemplo para mostrar el sitio.'

    def handle(self, *args, **options):
        user, creado = User.objects.get_or_create(
            username='demo', defaults={'email': 'demo@solucionesya.com', 'first_name': 'Usuario',
                                       'last_name': 'Demo'})
        if creado:
            user.set_password('demo12345')
            user.save()
        for titulo, subtitulo, cat, contenido, fecha in DATOS:
            Servicio.objects.get_or_create(
                titulo=titulo, defaults={'subtitulo': subtitulo, 'categoria': cat,
                                         'contenido': contenido, 'fecha': fecha, 'autor': user})
        self.stdout.write(self.style.SUCCESS(
            'Datos cargados. Usuario: demo / Contraseña: demo12345'))
