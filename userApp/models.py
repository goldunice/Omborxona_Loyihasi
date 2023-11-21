from django.db import models
from django.contrib.auth.models import AbstractUser


class Ombor(AbstractUser):
    ism = models.CharField(max_length=255, blank=True)
    nom = models.CharField(max_length=255, blank=True)
    manzil = models.CharField(max_length=255, blank=True)
    soha = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=255, blank=True)
    rasm = models.FileField(blank=True, null=True)
    logo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.ism
