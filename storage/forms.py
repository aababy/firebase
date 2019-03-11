from django import forms
from django.forms import ModelForm  
from .models import App, Graph, Category 

class AppForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['version'].disabled = True

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['cover'].queryset = Graph.objects.filter(category=self.instance)
        