from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    # Add a root URL that redirects to the game app
    path('', RedirectView.as_view(url='/game/', permanent=True)),
]