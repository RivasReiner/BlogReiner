from django.conf.urls import url, include
from apps.principal.views import index,inicio,dark

from django.urls import include, path

app_name = "base";

urlpatterns = [
url(r'^$', index,name='index'),
url(r'^inicio$', inicio,name='inicio'),
url(r'^dark$', dark,name='dark'),
]