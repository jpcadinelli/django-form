from django.contrib import admin
from django.urls import path
from contato.views import contato, formulario_contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contato),
    path('contato/', formulario_contato, name='formulario_contato'),
]
