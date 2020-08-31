from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=8)