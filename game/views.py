from pyexpat import model
from typing import Any
from django import views
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views import View, generic
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


from.models import Empty

class IndexView(LoginRequiredMixin, View):
    model = Empty
    def get(self, request: Any) -> HttpResponse:
        return render(request,  "game/index.html")


class LoginView(generic.ListView):
    model = Empty
    template_name = "game/login.html"

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('game:index')
        else:
            return render(request, 'game/login.html', {'error': 'Invalid username or password'})
        

class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'game/register.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'game/register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=str(username), password=password, email=email)
        user.save()
        return redirect('login')
    

def logout_view(request):
    logout(request)
    return redirect('game:login')