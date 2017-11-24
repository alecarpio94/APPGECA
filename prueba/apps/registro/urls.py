from django.conf.urls import url
from ...apps.registro.views import *

urlpatterns = [

	url(r'^bienvenido/', bienvenido.as_view()),
	#url(r'^bienvenido_profesor/', bienvenido_prof.as_view()),

	####################LISTADOS PROFESOR#######################
	url(r'^listado_de_alumnoP/$', alumPListView.as_view(),name="alumno"),
	url(r'^listado_de_actividadesP/$', activPListView.as_view(),name="list_actividad"),
	
	######################REGISTROS ADMIN#######################
	url(r'^nuevo_alumno/$', Prueba.as_view() ,name="alumnoR"),
	url(r'^nuevo_profesor/$', profCreateView.as_view(), name = 'profesorR'),
	url(r'^nuevo_instrumento/$', instruCreateView.as_view(),name="instrumentoR"),
	url(r'^nueva_actividad/$', actiCreateView.as_view(),name="actividadR"),
	
	######################LISTADOS ADMIN########################
	url(r'^listado_de_alumno/$', alumListView.as_view(),name="list_alumno"),
	url(r'^movimiento_de_alumno/$', alumMListView.as_view(),name="list_alumnoM"),
	url(r'^listado_de_profesor/$', profListView.as_view(),name="list_profesor"),
	url(r'^movimiento_de_profesor/$', profMListView.as_view(),name="list_profesorM"),
	url(r'^listado_de_instrumento/$', instruListView.as_view(),name="list_instrumento"),
	url(r'^listado_de_actividades/$', activListView.as_view(),name="list_actividades"),

	#######################EDITAR DATOS##########################
	url(r'^editar/(?P<pk>\d+)$', alumUpdateView.as_view(),name='editar_alumno'),
	url(r'^editarP/(?P<pk>\d+)$', profUpdateView.as_view(),name='editar_profesor'),

	######################ELIMINAR DATOS#########################
	url(r'^borrar_alumno/(?P<pk>\d+)$',alumDeleteView.as_view(), name='eliminar_alumno'),
	url(r'^borrar_profesor/(?P<pk>\d+)$',profDeleteView.as_view(), name='eliminar_profesor'),

	#############################################################
	#url(r'^nuevo_alumno/alumno$', firstFormView.as_view() ,name="alumnoRR"),
	#url(r'^nuevo_alumno/vivienda$', secondFormView.as_view() ,name="viviendaR"),
	url(r'^ERROR_404/$', error404.as_view(),name="ERROR_404"),
] 
