from django.db import models

# Create your models here.
class bloging(models.Model):
    blogtitle = models.CharField(max_length=100)
    blogdesc = models.TextField()

    #the below line change the name in the admin page
    def __str__(self):
        return self.blogtitle