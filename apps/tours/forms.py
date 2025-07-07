from django import forms
from .models import PlaceCategory, Review


class PlaceCategoryForm(forms.ModelForm):
    class Meta:
        model = PlaceCategory
        fields = ['name', 'short_description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['email','fio','review','rating']