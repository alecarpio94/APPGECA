# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from ...apps.utils.mixins import AdminRequiredMixin,ProfesorRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.views.generic import ListView, TemplateView
# class based views.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View
# import mixins

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from .models import Users
from .forms import UsersModelForm, UsersUpdateModelForm
from django.contrib.auth.decorators import login_required
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'administrador/index.html'

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/page-login.html", { 'form': form })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/bienvenido/') 
            else:
                return render(request,"administrador/page-error.html")
        else:
            return redirect('/login/')
        return render(request)

class UsersCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Users
    form_class = UsersModelForm

# logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')