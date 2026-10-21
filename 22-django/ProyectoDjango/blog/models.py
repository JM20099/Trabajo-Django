from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    #Metodo str para que cuando se muestre el objeto imprima un string
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", verbose_name="Imagen", upload_to="articles")  #upload_to indica la carpeta donde se guardara la imagen
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE)    #Cascade significa que si se borra el usuario se borran sus articulos
    categories = models.ManyToManyField(Category, verbose_name="Categorías", blank=True, related_name="articles")  #Relacion muchos a muchos, un articulo puede tener muchas categorias y una categoria puede tener muchos articulos                                
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación:")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created_at']  #Ordena los articulos por fecha de creacion, el mas reciente primero

    #Metodo str para que cuando se muestre el objeto imprima un string
    def __str__(self):
        return self.title
  
