from django.contrib import admin
from django.urls import path
from .views import CadastrarClienteCreateView


urlpatterns = [
    path('cadastrar/cliente', CadastrarClienteCreateView.as_view(), name="cadastrarCliente"),
]