from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")  # CharField es como un varchar y max_length es el tamaño máximo que puede tener
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to='articles')  # ImageField es para que podamos subir imágenes y upload_to es para que podamos guardar las imágenes en una carpeta llamada articles
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")  # auto_now_add=True hace que se guarde la fecha y hora en que se creó el objeto
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")  # auto_now=True hace que se guarde la fecha y hora en que se actualizó el objeto

    class Meta:
        # poner nombre en singular
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.title} {public}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.TextField(max_length=250)
    created_at = models.DateField()   # DateField es para que podamos guardar solo la fecha y los parentesis vacíos es para que nosotros coloquemos la fecha

    class Meta:
        # poner nombre en singular
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"