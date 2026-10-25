from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import Registerform

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })


# otra ruta
def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre Nosotros'
    })

def register_page(request):
    register_form = Registerform()

    if request.method == 'POST':
        register_form = Registerform(request.POST)

        if register_form.is_valid():
            register_form.save()

            return redirect('inicio/')

    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })