from django.urls import path
from . import views

urlpatterns = [
    path('character/create/', views.character_create, name='character_create'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
]