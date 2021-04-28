from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import Message, Contact
# Create your views here.



def contact(request):
    contact = Contact.objects.all()
    return render(request,'./contact/contact.html', {'contact': contact})
  
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        userMessage = Message(name=name, email=email, subject=subject, message=message)
        userMessage.save()
        messages.success(request,"Thank you for your message")
        return redirect('/./contact/contact')

