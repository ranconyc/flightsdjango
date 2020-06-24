from django.db import models

# Create your models here.
class Flight(models.Model):
  origin = models.CharFiled(max_length = 64)
  destination = models.CharFiled(max_length = 64)
  duration = models.IntegerFiled()
