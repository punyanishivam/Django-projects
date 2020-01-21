from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todo_view(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items':all_todo_items})

def add_item(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delete_item(request, item_id):
    item = TodoItem.objects.get(id = item_id)
    item.delete()
    return HttpResponseRedirect('/todo/')