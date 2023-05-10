from django import forms
from .models import *
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class Message(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20'}))
    txt = forms.CharField(widget=forms.Textarea(attrs={'col': 150, 'class': 'col-12 bo-rad-10 size35 bo2 txt10 p-l-20 p-t-15 m-b-10 m-t-3;'}),)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
    class Meta:
       model = Get_message
       fields = ("__all__")
