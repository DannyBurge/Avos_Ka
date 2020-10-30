from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path(r'admin/', admin.site.urls),
]

urlpatterns += [
    path(r'', include('homepage.urls')),
    path(r'shoplist/', include('ProductList.urls')),
    path(r'recepies/', include('Recepies.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]