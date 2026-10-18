from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)  # CharField es como un varchar y max_length es el tamaño máximo que puede tener
    content = models.TextField()
    image = models.ImageField(default='null')  # ImageField es para que podamos subir imágenes y upload_to es para que podamos guardar las imágenes en una carpeta llamada articles
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True hace que se guarde la fecha y hora en que se creó el objeto
    updated_at = models.DateTimeField(auto_now=True)  # auto_now=True hace que se guarde la fecha y hora en que se actualizó el objeto

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.TextField(max_length=250)
    created_at = models.DateField()   # DateField es para que podamos guardar solo la fecha y los parentesis vacíos es para que nosotros coloquemos la fecha
