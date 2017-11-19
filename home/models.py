from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
# Create your models here.
class Questions(models.Model):
    question=models.CharField(max_length=500)
    user=models.ForeignKey(User)

