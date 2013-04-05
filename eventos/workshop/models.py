class Evento(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="imgs/")


class Palestra(models.Modeel):
    nome_palestra = models.CharField(max_length=50)
    evento = models.ForeignKey(Evento)


class Participante(models.Model):
    nome_participante = models.CharField(max_length=50)
    palestra = models.ForeignKey(Palestra)
    avatar = models.ImageField(upload_to="imgs/")


class Palestrante(models.Model):
    nome_palestrante = models.CharField(max_length=50)
    palestra = models.ForeignKey(Palestra)
