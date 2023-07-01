from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    image = models.FileField(upload_to="picture")
    
