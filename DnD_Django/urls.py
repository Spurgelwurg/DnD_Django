from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    # Add a root URL that redirects to the login page if not authenticated
    path('', login_required(RedirectView.as_view(url='/game', permanent=True), login_url='game:login')),
]