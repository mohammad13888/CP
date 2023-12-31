from django import forms
from .models import PV_Member, Channel_Message

class Pv(forms.Form):
    username = forms.CharField(required=True)
class IMG(forms.Form):
    image=forms.ImageField(required=False)
    file=forms.FileField(required=False)
    content=forms.CharField(required=False)

class Chan(forms.Form):
    name = forms.CharField(required=True)

class EditUserProfile(forms.ModelForm):
    class Meta:
        model = PV_Member
        fields = ('display_name', 'bio', 'email')
class Chan_Message(forms.ModelForm):
    class Meta:
        model = Channel_Message
        fields = ('title','content','file')
