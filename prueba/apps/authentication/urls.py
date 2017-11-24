from django.conf.urls import url
from ...apps.authentication import views


import views

urlpatterns = [

	url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^add/$',views.UsersCreateView.as_view(), name='add'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
 
] 


