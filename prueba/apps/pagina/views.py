from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import os

this_path = os.getcwd() + '/polls/'

# Create your views here.
def inicio(request):
	
	return render (request, 'pagina/inicio.html')

def contact(request):
	
	return render (request, 'pagina/contacto.html')

def frecuente(request):
	
	return render (request, 'pagina/preguntas.html')

def somos(request):
	
	return render (request, 'pagina/resena.html')

def mision(request):
	
	return render (request, 'pagina/mision.html')

def calendario(request):
	
	return render (request, 'pagina/calendario.html')

#def eventos(request):
	
	#return render (request, 'pagina/eventos.xml')