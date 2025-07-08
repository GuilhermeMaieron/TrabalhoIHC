from django.db import models


class Lugar(models.Model):
    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    nome = models.CharField(max_length=256, unique=True)
    local = models.CharField(max_length=256)
    horario_abre = models.TimeField()
    horario_fecha = models.TimeField()
    foto = models.ImageField(upload_to='static/fotos_lugar/')
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome