from django.conf.urls import url
from ...apps.catedras import views

import views

urlpatterns = [

    url(r'^Clarinete/', views.catedra4),
    url(r'^Percusion/', views.catedra2),
    url(r'^Guitarra/', views.catedra3),  

] 
