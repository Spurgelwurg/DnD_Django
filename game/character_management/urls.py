from django.urls import path
from . import views

app_name = 'character_management'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('create/', views.character_create, name='character_create'),
    path('<int:character_id>/', views.character_detail, name='character_detail'),
    path('roll_dice/', views.roll_dice, name='roll_dice'),
    path('roll_ability_scores/', views.roll_ability_scores, name='roll_ability_scores'),
    path('get_subrace/', views.get_subrace, name='get_subrace'),
]