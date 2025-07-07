from django.urls import path

from apps.tours.views import hello_view, goodbye_view, category_list, create_category, create_review

urlpatterns = [
    path('index/', hello_view, name='index_view'),
    path('elements/', goodbye_view, name='elements_view'),
    path('generic/', category_list, name='category_list'),
    path('create_cat', create_category, name='create_category'),
    path('create_review', create_review, name='create_review'),

]