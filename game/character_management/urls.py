from django.urls import path
from . import views

app_name = 'character_management'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('create/<int:campaign_id>/', views.character_create, name='character_create'),
    path('<int:character_id>/', views.character_detail, name='character_detail'),
    path('roll_dice/', views.roll_dice, name='roll_dice'),
    #path('roll_ability_scores/',  name='roll_ability_scores'),
    path('get_subrace/', views.get_subrace, name='get_subrace'),

path('<int:character_id>/edit/', views.character_edit, name='character_edit'),
path('<int:character_id>/delete/', views.character_delete, name='character_delete'),
path('get_race_details/', views.get_race_details, name='get_race_details'),
path('get_class_details/', views.get_class_details, name='get_class_details'),
]