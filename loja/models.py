from django.db import models


class Cliente(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=255, verbose_name='Nome do cliente')
    cpf = models.CharField(null=False, blank=False, max_length=11, verbose_name='CPF')
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    data_hora_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    telefoneCliente = models.CharField(null=False, blank=False, max_length=11, verbose_name='Telefone')
    profissaoId = models.ForeignKey('Profissao', on_delete=models.DO_NOTHING, verbose_name='Profissao')
    sexoId = models.OneToOneField('Sexo', on_delete=models.DO_NOTHING, verbose_name='Sexo',
                                  primary_key=True, null=False, default=1)
    #redeSocialCliente = models.ForeignKey('RedeSocialCliente', verbose_name='Redes sociais', null=True, on_delete=models.DO_NOTHING)
    redeSocial = models.ForeignKey('RedeSocial', verbose_name='Rede social', null=True, on_delete=models.DO_NOTHING)
    username = models.CharField(null=False, blank=False, max_length=120, verbose_name='Perfil', default='')
    boolSegueALoja = models.BooleanField(blank=False, null=False, verbose_name='Segue a loja?', default=False)

    def __str__(self):
        return self.nome + '||' + self.pk


class Funcionario(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=255, verbose_name='Nome funcionario')
    cpf = models.CharField(null=False, blank=False, max_length=11, verbose_name='CPF')
    data_contratacao = models.DateField(blank=False, null=False, verbose_name='Data da contratação')
    data_demissao = models.DateField(blank=True, null=True, verbose_name='Data de demissão')
    bool_habilitacao = models.BooleanField(blank=False, null=False, verbose_name='Possui habilitação')
    cargoId = models.ForeignKey('Cargo', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Cargo')
    setorId = models.ForeignKey('Setor', on_delete=models.DO_NOTHING, blank=False, null=False,
                                verbose_name='Setor', default=1)
    usuario = models.CharField(null=False, blank=False, max_length=255, verbose_name='Usuário')
    senha = models.CharField(max_length=8, null=False, blank=False, verbose_name='Senha')




class Venda(models.Model):
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    bool_concluida = models.BooleanField(blank=False, null=False, verbose_name='Venda concluída?')
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor Total')
    # Relacionamentos
    vendaProdutoId = models.ManyToManyField('Produto')
    clienteId = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING)
    funcionarioId = models.ForeignKey('Funcionario', on_delete=models.DO_NOTHING)
    formaPagamentoId = models.OneToOneField('FormaPagamento', on_delete=models.DO_NOTHING)


class Produto(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=255, verbose_name='Descrição do produto')
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')
    estoque = models.IntegerField(verbose_name='Estoque', default=0, blank=False, null=False)
    dataCadastroProduto = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    categoriaProdutoId = models.ForeignKey('CategoriaProduto', on_delete=models.DO_NOTHING)
    marcaId = models.ForeignKey('Marca', on_delete=models.DO_NOTHING)


class CategoriaProduto(models.Model):
    pass


class Marca(models.Model):
    pass

class Sexo(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=9)

    def __str__(self):
        return self.descricao


class TelefoneCliente(models.Model):
    numeroTelefone = models.CharField(null=False, blank=False, max_length=11, verbose_name='Telefone')

    def __str__(self):
        return self.numeroTelefone

class RedeSocialCliente(models.Model):
    redeSocial = models.ForeignKey('RedeSocial', verbose_name='Rede Social##', on_delete=models.DO_NOTHING)
    username = models.CharField(max_length=255, blank=False, null=False, verbose_name='Username', default='')


    def __str__(self):
        return self.username


class RedeSocial(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=255, verbose_name='Rede Social')
    urlPrincipal = models.CharField(null=False, blank=False, max_length=255, verbose_name='URL Principal')

    def __str__(self):
        return self.descricao


class Profissao(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=255, verbose_name='Profissão', default='')

    def __str__(self):
        return self.descricao

class Setor(models.Model):
    pass


class Cargo(models.Model):
    pass


class FormaPagamento(models.Model):
    pass