from django.shortcuts import render

# Create your views here.

def catedra1(request):
	
	return render (request, 'catedras/catedra1.html')

def catedra2(request):
	
	return render (request, 'catedras/catedra2.html')

def catedra3(request):
	
	return render (request, 'catedras/catedra3.html')

def catedra4(request):
	 
	return render(request, 'catedras/catedra4.html')
