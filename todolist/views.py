from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import Todo
from django.utils import timezone

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context={'todo_list':todo_list}
    # return HttpResponse('보여주고싶은말 아무거나')
    return render(request, 'todolist/index.html', context)

def delete(request,todo_id):
    delete_id=Todo.objects.get(id=todo_id)
    delete_id.delete()
    todo_list = Todo.objects.all()
    context={'todo_list':todo_list}
    return render(request, 'todolist/index.html', context)
    
def add(request):
    q=Todo(todo=request.POST.get('todo'),is_complate=0,create_date=timezone.now())
    q.save()
    return redirect('/todolist/')


