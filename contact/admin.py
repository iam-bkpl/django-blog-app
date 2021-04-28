from django.contrib import admin
from . models import Contact, Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'subject')



admin.site.register((Contact,Message))
# admin.site.register(MessageAdmin)