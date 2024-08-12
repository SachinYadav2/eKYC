from django.db import models

# Create your models here.

class register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    place = models.CharField(max_length=40)
    