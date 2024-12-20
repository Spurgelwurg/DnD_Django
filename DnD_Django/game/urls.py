from django.urls import path

from game import views

app_name = "game"
urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
]