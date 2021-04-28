from django.db import models

# Create your models here.

class Service(models.Model):
    no = models.IntegerField()
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.TextField()


    def __str__(self):
        return self.title + "" + self.name
    