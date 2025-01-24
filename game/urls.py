from django.urls import path

from game import views

app_name = "game"
urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
     path("accounts/login/", views.LoginView.as_view(), name="login"),
     path('register/', views.RegisterView.as_view(), name='register'),
     path('logout/', views.logout_view, name='logout'),
]