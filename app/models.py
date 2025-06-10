from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=16)
    
    cep = models.CharField(max_length=9, blank=True)
    logradouro = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    localidade = models.CharField(max_length=100, blank=True)  # cidade
    uf = models.CharField(max_length=2, blank=True)
    numero_residencia = models.CharField(max_length=10, blank=True)
    
    # def __str__(self):
    #     return f"{self.nome} ({self.email})"
    

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='imagens/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome




   

class Venda(models.Model):
    cliente = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cartao = models.CharField(max_length=16)
    validade = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id} - {self.cliente.email} comprou {self.produto.nome}"
