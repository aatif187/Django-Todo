from django.shortcuts import redirect, render,get_object_or_404
from django.utils import timezone
from .models import Todo
# Create your views here.
def index(request):
    if request.method =='POST':
        
        new_todo= request.POST['newTodo']
        if not new_todo or len(new_todo)<3:
            return redirect('index')

        todoObj= Todo()
        todoObj.todo= new_todo
        todoObj.published_On=timezone.now()
        todoObj.save()
        return redirect('index')

    todos= Todo.objects.all()
    return render(request, 'index.html',{'todos':todos})

def delete(request,todo_id):
    print(request.method)
    if request.POST.get('delete'):
        todo= get_object_or_404(Todo, pk=todo_id)
        todo.delete()
        return redirect('index')
    if request.POST.get('complete'):
        todo= get_object_or_404(Todo, pk=todo_id)
        todo.is_Completed=True
        todo.save()
        return redirect('index')
    if request.POST.get('update'):
        return render(request, 'update.html',{'todo_id':todo_id})
    return redirect('index')

def update(request, todo_id):
    todo= get_object_or_404(Todo, pk=todo_id)
    todo.todo= request.POST['todo']
    todo.published_On=timezone.now()
    todo.save()
    return redirect('index')