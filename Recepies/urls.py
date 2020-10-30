from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.RecepieListView.as_view(), name="recepie"),
    url(r'^(?P<pk>\d+)$', views.RecepieDetailView.as_view(), name='recepie-detail'),
]
