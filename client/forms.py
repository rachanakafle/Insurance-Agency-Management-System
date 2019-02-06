from django import forms

from policy.models import Applied_Policy


class SigninForm(forms.ModelForm):
    policy_id = forms.IntegerField()
    Date_of_birth = forms.DateTimeField()

    class Meta:
        model = Applied_Policy
        fields = ['policy_id', 'Date_of_birth']

