from django.db import models

# Create your models here.
class info(models.Model):
    objects=models.Manager()
    Name=models.CharField(max_length=100, default='')
    Email=models.CharField(max_length=100, default='')
    Subject=models.CharField(max_length=100, default='')
    Message=models.CharField(max_length=100, default='')