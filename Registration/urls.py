from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url('registration', views.register_new_user, name='register'),
    path('', include('django.contrib.auth.urls')),

]
