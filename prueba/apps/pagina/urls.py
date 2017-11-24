from django.conf.urls import url
from ...apps.pagina import views

import views

urlpatterns = [

    url(r'^contacto/', views.contact),
    url(r'^preguntas/', views.frecuente),
    url(r'^quienes_somos/', views.somos),
    url(r'^mision_vision/', views.mision),
    url(r'^cronograma/', views.calendario),
    #url(r'^eventos/', views.eventos),

    url(r'^', views.inicio),  

] 
