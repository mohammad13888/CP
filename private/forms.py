from django import forms

class Pv(forms.Form):
    username = forms.CharField(required=True)
class IMG(forms.Form):
    image=forms.ImageField(required=False)
    file=forms.FileField(required=False)
    content=forms.CharField(required=False)

class Chan(forms.Form):
    name = forms.CharField(required=True)

