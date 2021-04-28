from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# from ckeditor.fields import RichTextField
# from tinymce.models import HTMLField
# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    # content = RichTextField(blank=True , null=True)
    content = models.TextField(blank=True, null=True)
    # content = HTMLField(blank=True, null=True)
    author = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return  self.title + ' by ' + self.author 
    