from django import forms

class Pv(forms.Form):
    username = forms.CharField(required=True)