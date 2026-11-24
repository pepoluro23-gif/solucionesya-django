from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    """Datos extra del usuario: avatar, biografía, teléfono y web."""
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='perfil')
    avatar = models.ImageField('Avatar', upload_to='avatares/', blank=True, null=True)
    bio = models.TextField('Sobre mí', blank=True)
    telefono = models.CharField('Teléfono', max_length=30, blank=True)
    web = models.URLField('Sitio web', blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'Perfil de {self.usuario.username}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_perfil(sender, instance, created, **kwargs):
    """Cada usuario nuevo tiene su perfil creado automáticamente."""
    if created:
        Perfil.objects.create(usuario=instance)
