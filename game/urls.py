from django.urls import path, include
from django.views.generic import TemplateView

app_name = "game"

urlpatterns = [
    path('', TemplateView.as_view(template_name='game/index.html'), name='index'),
    path('campaigns/', include('game.campaign_manager.urls', namespace='campaign_manager')),


]
