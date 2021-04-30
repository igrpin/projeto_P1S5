from django.db import models


class Cliente(models.Model):
    nome_Cliente_ = models.CharField(null=False, blank=False, max_length=255, verbose_name='Nome do cliente')
    cpf = models.CharField(null=False, blank=False, max_length=11, verbose_name='CPF')
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    data_hora_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    telefoneCliente = models.CharField(null=False, blank=False, max_length=11, verbose_name='Telefone')
    profissaoId = models.ForeignKey('Profissao', on_delete=models.DO_NOTHING, verbose_name='Profissao')
    sexoId = models.ForeignKey('Sexo', on_delete=models.DO_NOTHING, verbose_name='Sexo', null=False, default=1)
    #redeSocialCliente = models.ForeignKey('RedeSocialCliente', verbose_name='Redes sociais', null=True, on_delete=models.DO_NOTHING)
    redeSocial = models.ForeignKey('RedeSocial', verbose_name='Rede social', null=True, on_delete=models.DO_NOTHING)
    username = models.CharField(null=False, blank=False, max_length=120, verbose_name='Perfil', default='')
    boolSegueALoja = models.BooleanField(blank=False, null=False, verbose_name='Cliente segue a loja nessa rede?',
                                         default=False)
    uploadFoto = models.FileField(upload_to='media_cliente/', blank=True, null=True)

    def __str__(self):
        return str(self.pk) + ' ---||--- ' + self.nome


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


    def __str__(self):
        return self.nome


class Venda(models.Model):
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    bool_concluida = models.BooleanField(blank=False, null=False, verbose_name='Venda concluída?')
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor Total')
    vendaProdutoId = models.ManyToManyField('Produto')
    clienteId = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING)
    funcionarioId = models.ForeignKey('Funcionario', on_delete=models.DO_NOTHING)
    formaPagamentoId = models.ForeignKey('FormaPagamento', max_length=50, on_delete=models.DO_NOTHING)



    def __str__(self):
        return str(self.pk) + ' | ' + str(self.valor_total)


class Produto(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=255, verbose_name='Descrição do produto')
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')
    estoque = models.IntegerField(verbose_name='Estoque', default=0, blank=False, null=False)
    dataCadastroProduto = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    categoriaProdutoId = models.ForeignKey('CategoriaProduto', on_delete=models.DO_NOTHING, verbose_name='Categoria')
    marcaId = models.ForeignKey('Marca', on_delete=models.DO_NOTHING, verbose_name='Marca')


    def __str__(self):
        return self.descricao + ' | ' + str(self.marcaId) + ': R$' + str(self.preco)


class CategoriaProduto(models.Model):
    categoria = models.CharField(null=False, blank=False, max_length=255, verbose_name='Categoria')

    def __str__(self):
        return self.categoria


class Marca(models.Model):
    marca = models.CharField(null=False, blank=False, max_length=255, verbose_name='Marca')

    def __str__(self):
        return self.marca


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
    descricao = models.CharField(null=False, blank=False, max_length=255, verbose_name='Setor')

    def __str__(self):
        return self.descricao


class Cargo(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=255, verbose_name='Cargo')
    salario = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Salário')

    def __str__(self):
        return self.descricao


class FormaPagamento(models.Model):
    formaPagamento = models.CharField(null=False, blank=False, max_length=50, verbose_name='Forma de pagamento')

    def __str__(self):
        return self.formaPagamento

