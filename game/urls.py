from django.urls import path, include
from django.views.generic import TemplateView
from game import views

app_name = "game"
urlpatterns = [
    # Add this homepage URL
    path('', TemplateView.as_view(template_name='game/index.html'), name='index'),
    path('character/', include('game.character_management.urls')),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
]
