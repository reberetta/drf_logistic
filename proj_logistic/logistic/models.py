from django.db import models

class Logistic(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
