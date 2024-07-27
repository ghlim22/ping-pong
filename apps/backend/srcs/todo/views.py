from django.shortcuts import render

from . import models

# Create your views here.


def todo_list(request):
    todos = models.Todo.objects.filter(complete=False).order_by("created_at")
    return render(request, "todo/list.html", {"todos": todos})
