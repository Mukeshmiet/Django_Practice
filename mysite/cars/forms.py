from django import forms
from .models import Review
from django.forms import ModelForm

class reviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
    # first_name = forms.CharField(label='first_name', max_length=30)
    # last_name = forms.CharField(label='last_name', max_length=30)
    # email = forms.EmailField(label='email')
    # review = forms.CharField(label='any reviews!')