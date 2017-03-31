from django.views import generic
from .models import League

class IndexView(generic.ListView):
    template_name = 'leagues/index.html'

    def get_queryset(self):
        return League.objects.all()

class DetailView(generic.DetailView):
    model = League
    template_name = 'leagues/detail.html'
