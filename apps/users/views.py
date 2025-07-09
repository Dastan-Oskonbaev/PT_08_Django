
from django.shortcuts import render, redirect
from django.contrib import messages

from apps.users.forms import CustomUserCreationForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})