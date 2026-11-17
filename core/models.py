from django.db import models

class Guia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='guias/')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Guia'
        verbose_name_plural = 'Guias'

    def __str__(self):
        return self.nome

class Experiencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='experiencias/')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

    def __str__(self):
        return self.nome
