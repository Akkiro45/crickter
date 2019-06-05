# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def logoutUser(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('/')
    else:
        return HttpResponseRedirect('auth/login/')


def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create(
            # first_name = username,
            email = email,
            username = username
            )
        user.set_password(password)
        user.save()

        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/')
    else:
        return render(request,'authenapp/reg.html')   

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'authenapp/login.html')

