from django.contrib import admin

from .models import Servicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'fecha')
    list_filter = ('categoria', 'fecha')
    search_fields = ('titulo', 'subtitulo', 'contenido')
    date_hierarchy = 'fecha'
