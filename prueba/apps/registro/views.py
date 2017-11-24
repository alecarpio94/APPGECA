#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic import View
#________________________________________
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.template import Context
from django.template.context import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import CreateView 
from django.views.generic import ListView 
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
#paginacion de django#
from ...apps.registro.models import *
from ...apps.registro.forms import *
from ...apps.authentication.models import Users
from ...apps.utils.mixins import AdminRequiredMixin, ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

######################INICIO ADMIN######################
@method_decorator(login_required, name='dispatch')
class bienvenido(LoginRequiredMixin, TemplateView):
	
    template_name = ('administrador/index.html')

#####################ALUMNO ADMIN#######################
class Prueba(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	model = Alumno
	form_class =  AlumForm
	second_form_class = RepreForm 
	three_form_class = VivienForm 
	four_form_class = DireccForm
	five_form_class = FamiliForm 
	six_form_class = EducaForm
	seven_form_class = EmpreForm
	eight_form_class = EducaMusiForm
	night_form_class = PercRepreForm
	ten_form_class = PercAlumForm
	template_name = 'alumno/crear-alumno.html'

	def get_context_data(self, **kwargs):
	    context = super(Prueba, self).get_context_data(**kwargs)
	    context['alumno'] = self.form_class
	    context['representante'] = self.second_form_class
	    context['vivienda'] = self.three_form_class
	    context['direccion'] = self.four_form_class
	    context['familia'] = self.five_form_class
	    context['educacion'] = self.six_form_class
	    context['empresa'] = self.seven_form_class
	    context['educacusi'] = self.eight_form_class
	    context['percrepre'] = self.night_form_class
	    context['percalum'] = self.ten_form_class
	    return context   


class alumListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listasalumno'
	model = Alumno
	template_name = 'alumno/list-alumno.html'

class alumMListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listasalumno'
	model = Alumno
	template_name = 'alumno/mostr-alumno.html'

class alumUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'alumno/editar-alumno.html'
	model = Alumno
	fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo_alumno', 'fecha_nacimiento', 'lugar_nacimiento', 'nacionalidad', 'institucion'
		]
	success_url = '/listado_de_alumno/'

class alumDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	
	model = Alumno
	template_name = 'alumno/alumno_confirm_delete.html'
	success_url = reverse_lazy('registro:list_alumno')

########################################################

##################INSTRUMENTO ADMIN#####################
class instruCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	template_name = 'instrumentos/crear-instrumento.html'
	model = Instrumento
	fields = ['nombr_instr' , 'stock_min' , 'stock_max', 'uso',]
	success_url = '/listado_de_instrumento/'

class instruListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listainstrumento'
	model = Instrumento
	template_name = 'instrumentos/list-instrumentos.html'
########################################################

######################PROFESOR ADMIN####################
class profCreateView(LoginRequiredMixin,AdminRequiredMixin, CreateView):
	model = Profesor
	fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor', 'asignacion']
	template_name = 'profesor/crear-profesor.html'
	success_url = '/listado_de_profesor/'

class profListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listaprofesor'
	model = Profesor
	template_name = 'profesor/list-profesor.html'

class profMListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listaprofesor'
	model = Profesor
	template_name = 'profesor/mostr-profesor.html'

class profUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'profesor/editar-profesor.html'
	model = Profesor
	fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor', 'asignacion']
	success_url = '/listado_de_profesor/'

class profDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):

	model = Profesor
	template_name = 'profesor/profesor_confirm_delete.html'
	success_url = reverse_lazy('registro:list_profesor')

########################################################

######################ACTIVIDAD ADMIN####################
class actiCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	model = Actividad
	fields = ['codigo_act', 'nombr_acti', 'descripcio', 'fecha_inic', 'fecha_fina']
	template_name = 'actividades/crear-actividad.html'
	success_url = '/listado_de_actividades/'

class activListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listasactividades'
	model = Actividad
	template_name = 'actividades/list-actividad.html'

class activCalendar(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Calendar'
	model = Actividad
	template_name = 'pagina/events.xml'
		
########################################################

####################MOSTRAR PROFESOR#####################
class activPListView(ListView):
	context_object_name = 'Listasactividades'
	template_name = 'admin_profesor/list-actividadP.html'

class alumPListView(ListView):
	context_object_name = 'Listasactividades'
	model = Alumno
	template_name = 'admin_profesor/list-alumnoP.html'

class error404(TemplateView):
	template_name = 'administrador/page-error.html'
		