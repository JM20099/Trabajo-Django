from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import Registerform
from django.contrib.auth import authenticate, login, logout


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

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form = Registerform()

        if request.method == 'POST':
            register_form = Registerform(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Se ha Registrado Correctamente!!!')

                return redirect('inicio')
            
        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
            return redirect('inicio')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.success(request, 'No ha podido iniciar sesion!!!')
        
        return render(request, 'users/login.html', {
            'title': 'Identificate'
        })

def logout_user(request):
    logout(request, )
    return redirect('login')