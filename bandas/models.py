

from django.db import models

class Evento(models.Model):
    local = models.CharField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.local