from django.contrib import admin
from .models import Alumnos #Importa la clase definida en models
from .models import Comentario
from .models import ComentarioContacto


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('matricula', 'nombre', 'carrera', 'turno', 'created')   #daremos formato a la tabla de alumnos separando en columnas
    search_fields=('matricula', 'nombre', 'carrera', 'turno')  #agregando un formulario de búsqueda
    date_hierarchy='created'    # agregando búsqueda por fecha
    list_filter=('carrera', 'turno') 
# Grupos de permisoso de usuario para acceso al modulo administracion
def get_readonly_fields(self, request, obj=None):
    if request.user.groups.filter(name="Usuarios").exists():
        return ('created', 'update', 'matricula', 'carrera', 'turno')
    else:
        return ('created', 'update')


admin.site.register(Alumnos, AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display=('id', 'coment')
    search_fields=('id', 'created')
    date_hierarchy='created'
    readonly_fields=('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display=('id', 'mensaje')
    search_fields=('id', 'created')
    date_hierarchy='created'
    readonly_fields=('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)


