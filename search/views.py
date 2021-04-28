from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.


def search(request):
    query = request.GET['query']
    if len(query)>100:
        allPost = Post.objects.none()
    else:    
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsBlog = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)

        allPosts = allPostsTitle.union(allPostsBlog,allPostsAuthor)

    params = {'allPosts': allPosts, 'query':query}
    return render(request,'./search/search.html',params)
