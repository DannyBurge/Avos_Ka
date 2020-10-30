from django.conf.urls import url
from .views import show_list

urlpatterns = [
    url(r'^$', show_list, name="shoplist"),
]
