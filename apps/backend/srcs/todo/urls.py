from django.urls import path

from . import views

app_name = "todo"

url_patterns = [path("list/", views.todo_list, name="list")]
