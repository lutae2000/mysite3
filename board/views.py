from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from board.models import Board


def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list':board_list}
    return render(request, 'board/list.html', context)
#user
#count


def write(request):
    return render(request, 'board/write.html')

def modify(request):
    content = Board.objects.filter(id=request.GET['id'])
    context = {'context',content}
    return render(request, 'board/modify.html',context)

def add(request):
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.save()
    return HttpResponseRedirect('/board/list')

def view(request):
    content = Board.objects.filter(id=request.GET['id'])

    context = {'content':content}
    print(context)

    return render(request, 'board/view.html',context)
