from django.contrib import admin
from django.urls import path
from inicio import views as inicio_views
from registros import views as registros_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs de la app 'inicio'
    path('contacto/', inicio_views.contacto, name="Contacto"),
    path('formulario/', inicio_views.formulario, name="Formulario"),
    path('ejemplo/', inicio_views.ejemplo, name="Ejemplo"),

    # URL principal que apunta a registros
    path('', registros_views.registros, name="Principal"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)

