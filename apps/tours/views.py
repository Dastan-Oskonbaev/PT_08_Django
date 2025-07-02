from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    return render(request, 'index.html')


def goodbye_view(request):
    return render(request, 'generic.html')