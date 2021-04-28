from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth   
from django.contrib import messages

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if User.objects.filter(username = username).exists():
            messages.info(request,'Username is already taken')
            return redirect('register')

        elif User.objects.filter(email = email).exists():
            messages.info(request, "Email is already taken")
            return redirect('register')


        else:
            if password == repeatPassword:
                user = User.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name,)
                user.save()
                return redirect('login')

            else:
                messages.info(request, "Password didn't match")
                return redirect('register')



    elif request.method == 'GET':
        return render(request,'./accounts/register.html')


def login(request):
    if request.method =='GET':
        return render(request, './accounts/login.html')

    else:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username or Password didn't match")
            return redirect('login')

        

def logout(request):
    auth.logout(request)
    return redirect('/')

