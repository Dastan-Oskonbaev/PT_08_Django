from django.urls import path

from apps.users.views import *

urlpatterns = [
    path('register/', register_view, name='register')
]