from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic

from.models import Empty

class IndexView(generic.ListView):
    model = Empty
    template_name = "game/index.html"

# def simple_view(request):
#     return HttpResponse("Hello, world!")