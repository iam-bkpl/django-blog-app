from django.db import models
from django.utils.timezone import now
# Create your models here.

class Contact(models.Model):
    phone = models.IntegerField(max_length=13)
    phonePerson =models.TextField()
    email = models.EmailField(max_length=254)
    emailPerson = models.TextField()
    location = models.TextField(blank=True)
    map = models.TextField(blank=True)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return "Name = " + self.name + " Email =  " + self.email 


