from django.urls import path, include
from django.views.generic import TemplateView

app_name = "game"
urlpatterns = [
    # Add this homepage URL
    path('', TemplateView.as_view(template_name='game/index.html'), name='index'),
    path('character/', include('game.character_management.urls')),
]