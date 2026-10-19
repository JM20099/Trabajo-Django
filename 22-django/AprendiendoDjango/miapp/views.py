from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category

# Create your views here.
# MVC = Modelo    Vista    Controlador  -> ACcciones (metodos)
# MVT = Modelo   Template  Vista   -> Acciones (metodos)



def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "<ul>"

    nombre = 'Carlos Gomez'
    lenguajes = ['Python', 'JavaScript', 'Java', 'C#']

    return render(request, 'index.html', {
        'title': "Inicio",
        'mi_variable': "Soy un dato que esta en la vista",
        'nombre': nombre,
        'lenguajes': lenguajes,
    })

def hola_mundo(request):
    return render(request, 'hola_Mundo.html')
        

def pagina(request, redirigir = 0):
    if redirigir == 1:
        return redirect('/inicio/')

    return render(request, 'pagina.html')

def contacto(request, nombre = "", apellidos= ""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p/"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse("<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
        )
    articulo.save()  # Guardar el articulo en la base de datos
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")


# Hacer consultas a la base de datos
def articulo(request):

    try:
        articulo = Article.objects.get(title="Matrix", public=False)  # Obtener el articulo con id 1
        response = (f"Articulo:<br/>{articulo.id} {articulo.title}")
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)  # Obtener el articulo con id

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()  

    return HttpResponse(f"Articulo {articulo.id} actualizado: {articulo.title} - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all()  # Obtener todos los articulos

    articulos = Article.objects.filter(title__exact="Articulo")  # obtener todos los articulos con el titulo exacto "Batman"
    
    articulos = Article.objects.filter(
                                    title="Articulo", 
                                   ).exclude(public=True)  # obtener todos los articulos con el titulo exacto "Batman" y que no sean publicos
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=0")  # obtener todos los articulos con el titulo exacto "Batman" y que no sean publicos
    
    return render(request, 'articulos.html',
                  {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)  # Obtener el articulo con id
    articulo.delete()  # Borrar el articulo

    return redirect('articulos')  # Redirigir a la vista de articulos


#Copia de crear_articulo y lo llamamos save_article
def save_article(request):     # No pasamos parametros por url y lo vamos a pasar por formulario
    if request.method == 'POST':
        title = request.POST['title']
        if len(title) < 5:
            return HttpResponse(f"El titulo es muy pequeño")
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title, #title(nombre del modelo) = title(nombre de la variable)
            content = content,
            public = public
        )
        #Para guardar este articulo en la BD
        articulo.save()
        return HttpResponse(f"Artículo creado: <strong> {articulo.title} - {articulo.content} </strong>")
    else:
        return HttpResponse(f"<h2> No se ha podido crear el articulo </h2>")

def create_article(request):
    return render(request, 'create_article.html')