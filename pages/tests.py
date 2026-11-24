from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Servicio


class ServicioTests(TestCase):
    def setUp(self):
        self.autor = User.objects.create_user('autor', password='clave12345')
        self.otro = User.objects.create_user('otro', password='clave12345')
        self.servicio = Servicio.objects.create(
            titulo='Placard Rehau test', subtitulo='Prueba', contenido='<p>Texto</p>',
            autor=self.autor)

    def test_lista_vacia_muestra_mensaje(self):
        Servicio.objects.all().delete()
        r = self.client.get(reverse('pages:lista'))
        self.assertContains(r, 'No hay páginas aún')

    def test_buscador(self):
        r = self.client.get(reverse('pages:lista'), {'q': 'rehau'})
        self.assertContains(r, 'Placard Rehau test')
        r = self.client.get(reverse('pages:lista'), {'q': 'zzz'})
        self.assertNotContains(r, 'Placard Rehau test')

    def test_crear_requiere_login(self):
        r = self.client.get(reverse('pages:crear'))
        self.assertEqual(r.status_code, 302)

    def test_solo_autor_puede_editar(self):
        self.client.login(username='otro', password='clave12345')
        r = self.client.get(reverse('pages:editar', args=[self.servicio.pk]))
        self.assertEqual(r.status_code, 403)
        self.client.login(username='autor', password='clave12345')
        r = self.client.get(reverse('pages:editar', args=[self.servicio.pk]))
        self.assertEqual(r.status_code, 200)

    def test_about(self):
        self.assertEqual(self.client.get(reverse('pages:about')).status_code, 200)
