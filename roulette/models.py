from django.db import models

class Roulette(models.Model):
    title = models.CharField("Name", max_length=255)