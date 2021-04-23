from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Cliente
from django.urls import reverse_lazy


class CadastrarClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cadastrarCliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("cadastrarCliente")