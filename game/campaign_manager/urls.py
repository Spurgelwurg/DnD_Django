from django.urls import path
from . import views

app_name = "campaign_manager"

urlpatterns = [

    path('', views.campaigns_view, name='campaigns'),
    path('campaigns/', views.campaigns_overview, name='campaigns_overview'),
    path('list/', views.campaign_list, name='campaign_list'),
    path('create/', views.campaign_create, name='campaign_create'),
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('<int:campaign_id>/edit/', views.campaign_edit, name='campaign_edit'),
    path('<int:campaign_id>/npc/create/', views.npc_create, name='npc_create'),
    path('npc/<int:npc_id>/edit/', views.npc_edit, name='npc_edit'),
    path('<int:campaign_id>/event/create/', views.event_create, name='event_create'),
    # Füge weitere URLs für Villains, Locations, etc. hinzu
]
