from django.db import models

# Create your models here.

DEQUEM =([1,"Dri"], [2,"Li"], [3,"Neide"], [4,"Bia"])

class Convite(models.Model):
    nome = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    convidados = models.FloatField(null=True, blank=True)
    convites = models.IntegerField(null=True, blank=True)
    dequem = models.IntegerField(choices=DEQUEM, null=True, blank=True)
    rspv = models.DateTimeField(null=True, blank=True)
    adultos = models.IntegerField(null=True, blank=True)
    criancas = models.IntegerField(null=True, blank=True)


