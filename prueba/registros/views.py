import datetime
from django.shortcuts import render,get_object_or_404
from .models import Alumnos, Comentario #Accedemos la modelo alumno que contiene la estructura de la tabla
from .forms import ComentarioContactoForm, ArchivosForm
from .models import ComentarioContacto, Archivos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q



""" def registros (request):
    alumnos=Alumnos.objects.all() #all recupera todos los objetos del modelo(registros de la tabla alumnos)
    return render(request, "registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados """


def registrar(request):
    if request.method == 'POST':
        form=ComentarioContactoForm(request.POST)
        if form.is_valid():  #si los datos recibidos son correctos
            form.save()  #inserta
            comentarios =ComentarioContacto.objects.all()
            return render (request, 'registros/comentarios.html',
                {'comentarios': comentarios})
    form=ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulariolos datos ingresados
    return render(request, 'registros/contacto.html', {'form':form})


def contacto(request):
    return render(request, "registros/contacto.html")
    #Indicamos el lugar donde se realizara el resultado de esta vista


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/comentarios.html",
                      {'comentarios':comentarios})
    return render(request, confirmacion, {'object': comentario})


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",
        {'comentarios':comentarios}) 
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render (request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render (request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera","turno","imagen")
    return render (request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains="Vespertino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=["luis", "barter"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

# Consultas por fecha
def consultar6(request):
    fechaInicio = datetime.date(2021, 7, 8)
    fechaFin = datetime.date(2021, 7, 9)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


# A. consultar por 14 de Julio
def comentarios_por_fecha(request):
    #Estabecemos el rango de fechas
    fecha_inicio = datetime.date(2025, 7, 8)
    fecha_fin = datetime.date(2025, 7, 9)

    #Filtrar comentarios que su fecha de creacion este en este rango
    comentarios = ComentarioContacto.objects.filter(
        created__date__range=(fecha_inicio, fecha_fin)
    )

    ##Renderizar una plantilla html pasandole los comentarios encontrados
    return render (request, 'registros/comentarios.html', {'comentarios': comentarios})

def buscar_comentario(request):
    #definimos la expresion a buscar en el comentario
    expresion = "felicidades" #palabra que sera buscada dentro de cada mensaje de la base de datos comentarioContacto
    #Usamos filter para obtener solo los comentarios que contienen esa palabra
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains = expresion)
#el 'mensaje__icontains' => busca que el campo 'mensaje' contenga ''felicidades'
    #Retirnamod la plantilla donde se vera esta consulta
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

@login_required
def comentarios_del_usuario(request):
    nombre_usuario = request.user.username
    comentarios = ComentarioContacto.objects.filter(usuario__iexact=nombre_usuario)
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def obtener_comentarios():
    comentarios = ComentarioContacto.objects.values_list('mensaje', flat=True)
    return comentarios

def empiezaPor(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="Soy")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})


def archivos(request):
    # Si se envió el formulario (método POST)
    if request.method == 'POST':
        # Instancia el formulario con los datos y archivos enviados
        form = ArchivosForm(request.POST, request.FILES)

        # Si el formulario es válido (todos los campos requeridos están bien)
        if form.is_valid():
            # Obtiene los datos del formulario
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']

            # Crea una instancia del modelo Archivos con los datos, aqui modifica la tabla
            nuevo_archivo = Archivos(
                titulo=titulo,
                descripcion=descripcion,
                archivo=archivo
            )

            # Guarda el archivo en la base de datos
            nuevo_archivo.save()

            # Renderiza la misma página (puedes redirigir si prefieres)
            return render(request, "registros/archivos.html")

        else:
            # Si hay errores, muestra un mensaje
            messages.error(request, "Error al procesar el formulario")

    # Si la petición no es POST, simplemente muestra la página y los archivos
    archivos = Archivos.objects.all()  # Obtiene todos los archivos para mostrar
    return render(request, "registros/archivos.html", {
        'archivo': archivos
    })



def consultasSQL(request):
    alumnos=Alumnos.objects.raw( 'SELECT id,  matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera ="TI" ORDER BY turno DESC')
    return render (request, "registros/consultas.html",
    {'alumnos': alumnos})

""" //TODO: """
def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render (request, "registros/seguridad.html",
    {'nombre': nombre})


def registros(request):
    query = request.GET.get('q') 
    if query:   
        alumnos = Alumnos.objects.filter(
            Q(nombre__icontains=query) | Q(matricula__icontains=query)
        )
    else:
        alumnos = Alumnos.objects.all()  
    return render(request, "registros/principal.html", {'alumnos': alumnos, 'query': query})  
