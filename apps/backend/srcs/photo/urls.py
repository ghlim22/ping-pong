from django.urls import path

from . import views

app_name = "photo"

urlpatterns = [
    path("list/", views.photo_list, name="list"),
    path("detail/<int:pk>/", views.photo_detail, name="detail"),
    path("create/", views.photo_create, name="create"),
    path("update/<int:pk>", views.photo_update, name="update"),
]
