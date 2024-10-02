# myapp/models.py
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    favorite_color = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    favorite_animal = models.CharField(max_length=100)

    def __str__(self):
        return self.name
