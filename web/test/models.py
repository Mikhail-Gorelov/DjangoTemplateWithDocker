from django.db import models
from django.contrib.auth import get_user_model
from . import managers

class Test(models.Model):
# Create your models here.
    text = models.CharField(max_length=120)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
