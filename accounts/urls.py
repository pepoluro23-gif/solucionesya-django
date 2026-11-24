from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.RegistroView.as_view(), name='registro'),
    path('login/', views.IngresoView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.PerfilView.as_view(), name='perfil'),
    path('profile/editar/', views.editar_perfil, name='editar_perfil'),
    path('profile/password/', views.CambiarPasswordView.as_view(), name='cambiar_password'),
]
