from django.db import models

# Create your models here.


class alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(null = False)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
