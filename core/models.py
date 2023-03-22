from django.db import models

# Create your models here.
class Topico(models.Model):
    nome = models.CharField(max_length=50)
    ordem = models.IntegerField()

    def __str__(self):
        return f'{self.ordem}. {self.nome}'

class Conteudo(models.Model):
    descricao = models.CharField(max_length=200)
    ordem = models.IntegerField()
    topico = models.ForeignKey(Topico, related_name='conteudos', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao}'

class Conversor(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tipo}'

class Limite(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tipo}'
        