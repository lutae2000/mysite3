from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook
# Create your views here.

def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list':guestbook_list}
    return render(request, 'guestbook/list.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.message = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/list')

def delete(request):
    # guestbook = Guestbook()
    # passwd = request.POST.get('password')
    # form_passwd =
    # if befor    e_id == passwd:
    #     guestbook.delete()
    # #delete from guestbook where form_passwd = passwd

    count = Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['pass']).count()

    if count != 0:
        Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['pass']).delete()
    # Guestbook.save()
    return HttpResponseRedirect('/list')

def deleteform(request):
    id = request.GET.get('id')
    context = {'id': id}
    return render(request, 'guestbook/deleteform.html',context)