from django import forms


class reviewForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=30)
    last_name = forms.CharField(label='last_name', max_length=30)
    email = forms.EmailField(label='email')
    review = forms.CharField(label='any reviews!')