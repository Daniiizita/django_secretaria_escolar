from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    serie = models.CharField(max_length=50)
    tipo_educacao = models.CharField(max_length=50)
    # adicione mais campos se necessário

# Create your models here.
