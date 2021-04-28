from django.shortcuts import render
from django.http import HttpResponse
from .models import Program 

# Create your views here.
program = Program.objects.all()


def index(request):
    return render(request, './home/index.html', {'programs' : program})

def about(request):
    return render(request,'./home/about.html')
