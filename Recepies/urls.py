from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.RecepieListView.as_view(), name="recepie"),
    url(r'^(?P<pk>\d+)$', views.RecepieDetailView.as_view(), name='recepie-detail'),
    url(r'^myrecepies/$', views.RecepiesByUserListView.as_view(), name='my-recepies'),
    url(r'^myrecepies/add', views.add_recepie, name='add-recepie'),
]
