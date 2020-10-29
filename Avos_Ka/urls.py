from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('shoplist/', include('ProductList.urls')),
    path('recepies/', include('Recepies.urls')),
    path('', include('homepage.urls')),

]
