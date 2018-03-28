from django import forms
from django.forms import ModelForm  
from .models import Graph, Tag 

class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['cover'].queryset = Graph.objects.filter(tag=self.instance)
        