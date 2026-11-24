from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('pages/', views.ServicioListView.as_view(), name='lista'),
    path('pages/nuevo/', views.ServicioCreateView.as_view(), name='crear'),
    path('pages/mios/', views.mis_servicios, name='mios'),
    path('pages/<int:pk>/', views.ServicioDetailView.as_view(), name='detalle'),
    path('pages/<int:pk>/editar/', views.ServicioUpdateView.as_view(), name='editar'),
    path('pages/<int:pk>/borrar/', views.ServicioDeleteView.as_view(), name='borrar'),
]
