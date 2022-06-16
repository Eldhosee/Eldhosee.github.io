from django.db import models
from django.forms import CharField

# Create your models here.
class add(models.Model):
    todo=models.CharField(max_length=30)
    def _str_(self):
        return self.todo

