from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from blog.models import Post
# Create your models here.

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null= True)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:15] + " by " + self.user.username
    