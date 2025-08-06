from django.db import models
# Create your models here.

class Alumnas(models.Model):
    matricula = models.CharField(max_length=12, verbose_name="Mat")
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alumna"
        verbose_name_plural = "Alumnas"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
from ckeditor.fields import RichTextField



class Alumnos(models.Model): #define la estructura de la tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat") #texto corto    #verbose_name: cambia los nombres de los campos
    nombre = models.TextField() #texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null = True, upload_to="foto", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:  #cambia el titulo del modelo y da un ordenamiento a los registros
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=["-created"]   #el menos indica que se ordenará del más reciente al más viejo

    
    def __str__(self):
        return self.nombre #indica que se mostrar el nombre como valor en la tabla
    


class Comentario(models.Model):
    id=models.AutoField(primary_key=True, verbose_name="Clave")
    alumno=models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment=RichTextField(verbose_name="Comentario")

    class Meta:  #cambia el titulo del modelo y da un ordenamiento a los registros
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering=["-created"]   #el menos indica que se ordenará del más reciente al más viejo
    
    def __str__(self):
        return self.coment #indica que se mostrar el nombre como valor en la tabla
    

###################################Modelo Comentario Contacto#######################################3
#Esta linea define un nuevo modelo de Django, que hereda de model.model, en pocas palabras estas diciendo que vas a crear una tabla en la base de datos llamada ComentarioContacto
class ComentarioContacto(models.Model):
#Esta linea crea el campo id, primary key osea llve primaria, "Clave" es el nombre que se mostrara para el admin, osease mas bonito para los humanos...
    id=models.AutoField(primary_key=True, verbose_name="Clave")
#Crear un campo usuario de textoLargo (TextFielD), verbose_name es para darle un nombre bonito para el humano, 
    usuario=models.TextField(verbose_name="Usuario")
#Crear campo de mensaje igual es para un texto largo (textField) y con verbose_name  le damos un nombre al usuario
    mensaje=models.TextField(verbose_name="Comentario")
#Este campo guarda la hora/fecha exacta de cuando se creo este comentario, suto_now_add = true es qeu se agregara automaticamnete la fecha y hora cuando se cree el registro y claro el verbose_name para que el humano sepa como se llama
    created=models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

#Esto es para dar configuraciones extra al modelo, 
#Verbose_name y verbose_name_plural, nombres personalizados para el modelo en el admin Django
    class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural="Comentarios Contacto"
#Esto nos dice que al mostrar una lista de comentarios se ordenara desde el mas reciente  al mas antigua
        ordering=["-created"]
#No nos podemos olvidar de esta funcion, define como se mostrar el modelos cuando se convierte a texto 
#Aqui se devueleve el contenido de mensaje, asi que si imprimes un comentario, veras el texto del comentario directamente
    def __str__(self):
        return self.mensaje 
################################### Fin Modelo comentarioContacti#######################################3

from django.db import models

class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo
