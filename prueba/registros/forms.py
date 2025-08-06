# Importa el módulo de formularios de Django
from django import forms

# Importa las clases base para crear formularios basados en modelos y personalizar widgets de archivos
from django.forms import ModelForm, ClearableFileInput

# Importa los modelos ComentarioContacto y Archivos desde el archivo models.py de la misma app
from .models import ComentarioContacto, Archivos


# ==== FORMULARIO PARA COMENTARIOS ====

# Define un formulario basado en el modelo ComentarioContacto
class ComentarioContactoForm(forms.ModelForm):
    # Configuración del formulario (sección Meta)
    class Meta:
        # Especifica qué modelo se va a usar para crear este formulario
        model = ComentarioContacto
        # Indica qué campos del modelo se incluirán en el formulario
        fields = ['usuario', 'mensaje']


# ==== WIDGET PERSONALIZADO PARA INPUT DE ARCHIVOS ====

# Crea un widget personalizado para inputs de tipo archivo
class CustomClearableFileInput(ClearableFileInput):
    # Redefine la plantilla HTML que se usa para mostrar el checkbox de "eliminar archivo" junto al archivo actual
    template_with_clear = (
        '<br><label for="%(clear_checkbox_id)s">'
        '%(clear_checkbox_label)s</label> %(clear)s'
    )


# ==== FORMULARIO PARA ARCHIVOS ====

# Define un formulario basado en el modelo Archivos
class ArchivosForm(ModelForm):
    class Meta:
        # Indica qué modelo se va a utilizar para este formulario
        model = Archivos
        # Qué campos del modelo se van a mostrar en el formulario
        fields = ['titulo', 'descripcion', 'archivo']
        # Personaliza los widgets (elementos visuales) para cada campo
        widgets = {
            # Al campo 'archivo' se le asigna el widget personalizado que permite limpiar el archivo cargado
            'archivo': CustomClearableFileInput,
        }
