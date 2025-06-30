from django.urls import path

from apps.tours.views import hello_view, goodbye_view

urlpatterns = [
    path('python/', hello_view),
    path('js/', goodbye_view),
]