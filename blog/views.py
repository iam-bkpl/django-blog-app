from django.shortcuts import render, HttpResponse, redirect     
from service.models import Service
from home.models import Program
# from . models import Post, BlogComment
from . models import Post
from comment.models import BlogComment
from django.contrib import messages
from blog.templatetags import extras

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
    comments = BlogComment.objects.filter(post=post)
    
    # post.views = post.views + 1
    # post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
            


    context = {'post': post,'comments':comments,'user' : request.user, 'replyDict' : replyDict}
    return render(request, 'blog/blogPost.html', context)

