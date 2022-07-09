from django.shortcuts import render,redirect
from blog.models import Post
from django.contrib import messages
from . models import BlogComment

# Create your views here.
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno= postSno)
        parentSno = request.POST.get('parentSno')

        if parentSno == "":
            comment = BlogComment(comment= comment, user= user, post= post)
            messages.success(request, "Comment has been posted successfully")
            comment.save()

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post ,parent=parent)
            comment.save()
            messages.success(request, "Reply has been posted successfully")
       

    return redirect(f"/blog/{post.slug}")
