from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def insert(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("Form successfully saved")
            except:
                pass
    form = UserForm()
    return render(request, 'student/index.html', {'form': form})


def show(request):
    user = User.objects.all()
    return render(request, 'student/show.html', {"user": user})


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('show')


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'student/edit.html', {'user': user})


def update(request, id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        form = UserForm(request.POST, instance=user)
        print(user)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('show')
        return render(request, 'student/edit.html', {'user': user})
