from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsTests(TestCase):
    def test_perfil_se_crea_con_el_usuario(self):
        u = User.objects.create_user('nuevo', password='clave12345')
        self.assertTrue(hasattr(u, 'perfil'))

    def test_registro_y_login(self):
        r = self.client.post(reverse('accounts:registro'), {
            'username': 'pepe', 'email': 'pepe@mail.com', 'first_name': 'Pepe', 'last_name': 'Gómez',
            'password1': 'ClaveSegura123', 'password2': 'ClaveSegura123'})
        self.assertRedirects(r, reverse('accounts:perfil'))
        self.assertTrue(User.objects.filter(username='pepe').exists())

    def test_logout_post(self):
        User.objects.create_user('x', password='clave12345')
        self.client.login(username='x', password='clave12345')
        r = self.client.post(reverse('accounts:logout'))
        self.assertEqual(r.status_code, 302)
