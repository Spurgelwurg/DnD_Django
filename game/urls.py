from django.urls import path, include
from django.views.generic import TemplateView
from game import views
from django.contrib.auth import views as auth_views

app_name = "game"

urlpatterns = [
    # Add this homepage URL
    path('', views.AuthView.as_view(), name='auth'),
    # path('', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
    # path('', TemplateView.as_view(template_name='game/index.html'), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='game/auth.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
    path('character/', include('game.character_management.urls')),
    path('campaign/', include('game.campaign_manager.urls')),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
