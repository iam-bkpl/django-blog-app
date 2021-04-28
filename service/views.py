from django.shortcuts import render
from . models import Service
from home.models import Program
# Create your views here.



def service(request):
    services = Service.objects.all()
    programs = Program.objects.all()
    return render(request,'./home/services.html',{'services':services,'programs':programs })
