# myapp/forms.py
from django import forms
from .models import Person

class NameSearchForm(forms.Form):
    name = forms.CharField(max_length=100, label="Enter your name")

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'favorite_color', 'favorite_food', 'favorite_animal']
