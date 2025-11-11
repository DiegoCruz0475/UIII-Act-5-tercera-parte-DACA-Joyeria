# UIII_joyeria_0475/backend_joyeria/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_joyeria.urls')), # <-- Agrega esta línea para incluir las URLs de tu app
]