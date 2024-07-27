from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models

# Create your views here.


def todo_list(request):
    todos = models.Todo.objects.filter(is_completed=False).order_by("created_at")
    return render(request, "todo/list.html", {"todos": todos})


def todo_detail(request, pk):
    todo = models.Todo.objects.get(id=pk)
    return render(request, "todo/detail.html", {"todo": todo})


def todo_create(request):
    if request.method == "POST":
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo:list")
    else:
        form = forms.TodoForm()
    return render(request, "todo/create.html", {"form": form})


def todo_edit(request, pk):
    target = get_object_or_404(models.Todo, pk=pk)
    if request.method == "POST":
        form = forms.TodoForm(request.POST, instance=target)
        if form.is_valid():
            target = form.save(commit=False)
            target.save()
            return redirect("todo:list")
    else:
        form = forms.TodoForm(instance=target)
    return render(request, "todo/create.html", {"form": form})


def todo_done_list(request):
    todos = models.Todo.objects.filter(is_completed=True).order_by("created_at")
    return render(request, "todo/done_list.html", {"todos": todos})


def todo_done(request, pk):
    target = get_object_or_404(models.Todo, pk=pk)
    target.is_completed = True
    target.save()
    return redirect("todo:list")


def todo_delete(request, pk):
    target = get_object_or_404(models.Todo, pk=pk)
    target.delete()
    return redirect("todo:list")
