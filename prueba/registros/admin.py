from django.contrib import admin
from .models import Alumnas
# Register your models here.


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    fields = ('matricula', 'nombre', 'carrera', 'turno', 'imagen')

admin.site.register(Alumnas, AdministrarModelo)

