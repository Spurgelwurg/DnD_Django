from django.urls import path, include
from django.views.generic import TemplateView
from game import views

app_name = "game"
urlpatterns = [
    # Add this homepage URL
    path('', views.indexView, name='index'),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('character/', include('game.character_management.urls')),
]
