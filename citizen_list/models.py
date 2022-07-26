from django.db import models
from django.urls import reverse

# Create your models here.

class Citizen(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    status = models.IntegerField(default=3)
    salary = models.IntegerField(default=50000)
    boss = models.IntegerField(default=1)

    def get_url(self):
        return reverse('citizen_info', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.age}'