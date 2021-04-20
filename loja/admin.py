from django.contrib import admin
from .models import Cliente, Sexo, TelefoneCliente, Profissao, \
    Funcionario, Setor, Cargo, RedeSocial, RedeSocialCliente


admin.site.register(Cliente)
admin.site.register(Sexo)
admin.site.register(TelefoneCliente)
admin.site.register(RedeSocialCliente)
admin.site.register(Profissao)
admin.site.register(Funcionario)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(RedeSocial)
