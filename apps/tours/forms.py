from django import forms
from .models import PlaceCategory

class PlaceCategoryForm(forms.ModelForm):
    class Meta:
        model = PlaceCategory
        fields = ['name', 'short_description']