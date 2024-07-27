from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models

# Create your views here.


def photo_list(request):
    photos = models.Photo.objects.all()
    return render(request, "photo/list.html", {"photos": photos})


def photo_detail(request, pk):
    photo = get_object_or_404(models.Photo, pk=pk)
    return render(request, "photo/detail.html", {"photo": photo})


def photo_create(request):
    if request.method == "POST":
        form = forms.PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect("photo:detail", pk=photo.pk)
    else:
        form = forms.PhotoForm()
    return render(request, "photo/create.html", {"form": form})


def photo_update(request, pk):
    photo = get_object_or_404(models.Photo, pk=pk)
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect("photo:detail", pk=photo.pk)
    else:
        form = forms.PhotoForm(instance=photo)
    return render(request, "photo/update.html", {"form": form})
