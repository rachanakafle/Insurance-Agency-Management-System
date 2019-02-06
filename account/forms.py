from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import MyUser


class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ['username','password']

class SignupForm(UserCreationForm):
    choice = forms.ChoiceField(choices=[('client', 'Client'), ('agent', 'Agent')])
    class Meta:
        model = MyUser
        fields = [ "full_name","email","choice"]

