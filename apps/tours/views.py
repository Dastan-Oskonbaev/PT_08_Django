from django.http import HttpResponse
from django.shortcuts import render

from apps.tours.models import PlaceCategory, Place


def hello_view(request):
    return render(request, 'index.html')


def goodbye_view(request):
    return render(request, 'elements.html')


def category_list(request):
    categories = PlaceCategory.objects.all()
    places = Place.objects.all()


    return render(request, 'generic.html', {'categories': categories, 'places': places})
