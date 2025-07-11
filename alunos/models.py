from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} ({self.sigla})'

class Cidade(models.Model):
    nome = models.CharField(max_length=80)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Alunos(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    dataNascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} - {self.cidade}'