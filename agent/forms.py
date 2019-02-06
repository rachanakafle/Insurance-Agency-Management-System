from django import forms

from agent.models import Agent


class SigninForm(forms.ModelForm):
    License_code = forms.IntegerField()
    Date_of_birth = forms.DateTimeField()

    class Meta:
        model=Agent
        fields=['License_code','Date_of_birth']