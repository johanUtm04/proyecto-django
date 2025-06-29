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
