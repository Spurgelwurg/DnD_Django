from django.urls import path

from game import views

app_name = "game"
urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
     path('create_campaign/', views.create_campaign, name='create_campaign'),
     path('create_npc/', views.create_npc, name='create_npc'),
     path('create_enemy/', views.create_enemy, name='create_enemy'),
     path('create_location/', views.create_location, name='create_location'),
     path('create_event/', views.create_event, name='create_event'),
     path('create_task/', views.create_task, name='create_task'),
     path('task_list/', views.task_list, name='task_list'),
     path('create_notes/', views.create_notes, name='create_notes'),
     path('create_file/', views.create_file, name='create_file'),
     path('notes/', views.notes_list, name='notes_list'),
     path('files/', views.file_list, name='file_list'),
     # path('simple/', views.simple_view, name='simple_view'),s
]