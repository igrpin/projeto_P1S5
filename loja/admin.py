from django.contrib import admin
from .models import Cliente, Sexo, TelefoneCliente, Profissao, \
    Funcionario, Setor, Cargo, RedeSocial, RedeSocialCliente, Venda, Produto, \
    CategoriaProduto, Marca, FormaPagamento


# admin.site.register(Cliente)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "profissaoId", "redeSocial", "username")


admin.site.register(Sexo)
admin.site.register(TelefoneCliente)
# admin.site.register(RedeSocialCliente)
admin.site.register(Profissao)
admin.site.register(Funcionario)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(RedeSocial)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(CategoriaProduto)
admin.site.register(Marca)
admin.site.register(FormaPagamento)