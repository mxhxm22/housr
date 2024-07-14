from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'address', 'bedrooms', 'bathrooms', 'sqft', 'photo']
