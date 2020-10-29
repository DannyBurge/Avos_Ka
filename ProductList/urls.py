from django.conf.urls import url
from .views import show_list

urlpatterns = [
    url('', show_list, name="shoplist"),
]
