from django.db import models

# Create your models here.

    
class kelas(models.Model):
    kelas1=models.CharField(max_length=40)
    kelas2=models.CharField(max_length=50)