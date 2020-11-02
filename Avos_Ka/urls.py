from django.contrib import admin
from django.urls import path, include
from .views import register_new_user

urlpatterns = [
    path(r'admin/', admin.site.urls),
]

urlpatterns += [
    path(r'', include('Homepage.urls')),
    path(r'shoplist/', include('ProductList.urls')),
    path(r'recepies/', include('Recepies.urls')),
]

urlpatterns += [
    path('accounts/', include('Registration.urls')),
]