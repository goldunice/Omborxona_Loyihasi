from django.db import models
from userApp.models import Ombor


class Mahsulot(models.Model):
    nom = models.CharField(max_length=255)
    brend = models.CharField(max_length=255)
    olchov = models.CharField(max_length=255)
    narx = models.PositiveIntegerField()
    miqdor = models.PositiveIntegerField()
    kelgan_sana = models.DateField(null=True, blank=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}, {self.brend}"


class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    qarz = models.PositiveIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism}, {self.nom}"
