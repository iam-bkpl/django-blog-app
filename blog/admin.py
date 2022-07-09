from django.contrib import admin
from .models import Post

# from .models import BlogComment
# # Register your models here.

# admin.site.register(BlogComment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

# admin.site.register(Post)
