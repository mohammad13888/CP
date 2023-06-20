from django import forms
from pkg_resources import require

class Channel(forms.Form):
    slug = forms.CharField(required=True)
    password=forms.PasswordInput()