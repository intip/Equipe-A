from django.db import models

class Evento(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="imgs/")

    def __str__(self):
        return self.titulo


class Palestra(models.Model):
    nome_palestra = models.CharField(max_length=50)
    evento = models.ForeignKey(Evento)

    def __str__(self):
        return self.nome_palestra


class Participante(models.Model):
    nome_participante = models.CharField(max_length=50)
    palestra = models.ForeignKey(Palestra)
    avatar = models.ImageField(upload_to="imgs/")

    def __str__(self):
        return self.nome_participante


class Palestrante(models.Model):
    nome_palestrante = models.CharField(max_length=50)
    palestra = models.ForeignKey(Palestra)

    def __str__(self):
        return self.nome_palestrante

class Contact(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    text = models.TextField()

    def __str__(self):
        return self.name
