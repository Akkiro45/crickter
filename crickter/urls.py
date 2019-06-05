from django.conf.urls import url
from .views import home, add, info

urlpatterns = [
    url(r'^$',  home),
    url(r'add/$', add),
    url(r'info/$', info)
]
