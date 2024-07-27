from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    path("list/", views.todo_list, name="list"),
    path("detail/<int:pk>/", views.todo_detail, name="detail"),
    path("create/", views.todo_create, name="create"),
    path("edit/<int:pk>", views.todo_edit, name="edit"),
    path("done_list/", views.todo_done_list, name="done_list"),
    path("done/<int:pk>/", views.todo_done, name="done"),
    path("delete/<int:pk>/", views.todo_delete, name="delete"),
]
