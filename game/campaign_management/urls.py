from django.urls import path
from . import views

app_name = 'campaign_management'

urlpatterns = [
    path('', views.CampaignListView.as_view(), name='campaign_list'),
    path('create/', views.campaign_create, name='campaign_create'),
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('<int:campaign_id>/edit/', views.campaign_edit, name='campaign_edit'),
    path('<int:campaign_id>/delete/', views.campaign_delete, name='campaign_delete'),
]