from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView

from apps.tours.forms import ReviewForm
from apps.tours.models import PlaceCategory, Place, Review


# def hello_view(request):
#     return render(request, 'index.html')

def is_staff_check(user):
    return user.is_staff

@user_passes_test(is_staff_check, login_url='login')
def goodbye_view(request):
    return render(request, 'elements.html')

@login_required
def category_list(request):
    categories = PlaceCategory.objects.all()
    places = Place.objects.all()

    return render(request, 'generic.html', {'categories': categories, 'places': places})


# def create_category(request):
#     if request.method == 'POST':
#         form = PlaceCategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category_list')
#         else:
#             return render(request, 'create_category.html', {'form': form})
#     else:
#         form = PlaceCategoryForm()
#         return render(request, 'create_category.html', {'form': form})


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            return render(request, 'create_review.html', {'form': form})
    else:
        form = ReviewForm()
        return render(request, 'create_review.html', {'form': form})


class PlaceListView(ListView):
    model = Place #(SELECT * FROM Place)
    template_name = 'index.html'
    context_object_name = 'places'


class PlaceDetailView(DetailView):
    model = Place #(SELECT * FROM Place WHERE id = 2)
    template_name = 'detail.html'
    context_object_name = 'place'


class CategoryCreateView(CreateView):
    model = PlaceCategory
    template_name = 'create_category.html'
    fields = ['name', 'short_description']
    success_url = reverse_lazy('category_list')



