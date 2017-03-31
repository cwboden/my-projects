from django.conf.urls import url
from . import views

app_name = 'leagues'

urlpatterns = [

    # /leagues/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /leagues/<id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]