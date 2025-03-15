from django.urls import path
from . import views

app_name = 'campaign_management'

urlpatterns = [
    path('', views.CampaignListView.as_view(), name='campaign_list'),
    path('create/', views.campaign_create, name='campaign_create'),
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('<int:campaign_id>/edit/', views.campaign_edit, name='campaign_edit'),
    path('<int:campaign_id>/delete/', views.campaign_delete, name='campaign_delete'),
    path('<int:campaign_id>/chapters/create/', views.chapter_create, name='chapter_create'),
    path('<int:campaign_id>/chapters/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('<int:campaign_id>/chapters/<int:chapter_id>/edit/', views.chapter_edit, name='chapter_edit'),
    path('<int:campaign_id>/chapters/<int:chapter_id>/delete/', views.chapter_delete, name='chapter_delete'),
    path('join/', views.campaign_join, name='campaign_join'),
    path('<int:campaign_id>/players/', views.manage_players, name='manage_players'),
    path('<int:campaign_id>/leave/', views.leave_campaign, name='leave_campaign'),
    path('campaigns/<int:campaign_id>/add-character/', views.add_character_to_campaign, name='add_character_to_campaign'),
]