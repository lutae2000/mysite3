from django.shortcuts import render
from django.http import HttpResponseRedirect
# from user.models import User
# Create your views here.



def joinform(request):
    return render(request, '/user/joinform.html')

def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()
    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')