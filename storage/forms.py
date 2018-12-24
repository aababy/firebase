from django import forms
from django.forms import ModelForm  
from .models import Graph, Category 

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['cover'].queryset = Graph.objects.filter(category=self.instance)
        