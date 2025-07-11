from django.urls import path

from apps.tours.views import goodbye_view, category_list, create_review, PlaceListView, PlaceDetailView, \
    CategoryCreateView

urlpatterns = [
    path('index/', PlaceListView.as_view(), name='index_view'),
    path('detail/<int:pk>', PlaceDetailView.as_view(), name='detail_view'),
    path('elements/', goodbye_view, name='elements_view'),
    path('generic/', category_list, name='category_list'),
    path('create_cat/', CategoryCreateView.as_view(), name='create_category'),
    path('create_review', create_review, name='create_review'),

]