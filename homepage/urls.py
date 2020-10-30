from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.show_homepage, name="home"),
    url(r'^myrecepies/$', views.RecepiesByUserListView.as_view(), name='my-recepies'),

]
