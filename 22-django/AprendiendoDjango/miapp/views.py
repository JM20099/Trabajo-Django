from django.shortcuts import render, HttpResponse, redirect


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
    return render(request, 'index.html')

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