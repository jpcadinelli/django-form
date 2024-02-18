from django.db import models

class Contato(models.Model):
    id_contato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField(max_length=355)