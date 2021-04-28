from django.shortcuts import render, HttpResponse           
from service.models import Service
from home.models import Program
from . models import Post
# Create your views here.

services = Service.objects.all()
programs = Program.objects.all()
allPosts = Post.objects.all()
content = {'allPosts' : allPosts}

def blog(request):

   
    return render(request, './blog/index.html',content)
    

def blogPost(request, slug):    
  
    # return HttpResponse(f"This is blog post :{slug}")
    post = Post.objects.filter(slug=slug).first()

    post.views += 1
    post.save()
    # comments = BlogComment.objects.filter(post=post)
    # content = {'post': post,'comments':comments}
    return render(request, 'blog/blogPost.html', {'post':post})
