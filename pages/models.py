from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Servicio(models.Model):
    """Cada publicación del sitio: un servicio o un trabajo realizado por Soluciones Ya."""

    CATEGORIAS = [
        ('muebles', 'Armado de muebles'),
        ('camaras', 'Instalación de cámaras'),
        ('tanques', 'Limpieza de tanques'),
        ('electricidad', 'Electricidad'),
        ('plomeria', 'Plomería'),
        ('otros', 'Otros'),
    ]

    titulo = models.CharField('Título', max_length=120)
    subtitulo = models.CharField('Subtítulo', max_length=200)
    categoria = models.CharField('Categoría', max_length=20, choices=CATEGORIAS, default='otros')
    contenido = CKEditor5Field('Contenido', config_name='default')
    imagen = models.ImageField('Imagen', upload_to='servicios/', blank=True, null=True)
    fecha = models.DateField('Fecha del trabajo', default=timezone.now)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='servicios', verbose_name='Autor')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha', '-creado']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pages:detalle', kwargs={'pk': self.pk})
