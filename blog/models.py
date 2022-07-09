from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# from ckeditor.fields import RichTextField
# from tinymce.models import HTMLField


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(blank=True)
    # views = models.IntegerField(default=0)
    # content = RichTextField(blank=True , null=True)
    # content = HTMLField(blank=True, null=True)
    
    
    def __str__(self):
        return  self.title + ' by ' + self.author 
    


# class BlogComment(models.Model):
#     sno = models.AutoField(primary_key=True)
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete= models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     parent = models.ForeignKey('self',on_delete=models.CASCADE, null= True)
#     timestamp = models.DateTimeField(default=now)
#     views = models.IntegerField(default=0)
    