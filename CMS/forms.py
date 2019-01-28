
from django import forms
from django.contrib.auth.forms import UserCreationForm

from CMS.models import Agent, MyUser, Client
from policy.models import Policy


class SignupForm(forms.ModelForm):
    choice = forms.ChoiceField(choices=[('client', 'client'), ('agent', 'agent')])

    class Meta:
        model =Policy
        fields = ["policy_id", "choice"]


class SigninForm(forms.Form):


    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    choice = forms.ChoiceField(choices=[('client', 'client'), ('agent', 'agent')])

    class Meta:
        fields = ['username','password','choice']


class AgentForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields=['License_code','Name','gender','photo','Temporary_Address','Permanent_address',
                'Contact_number','Email','password','Nationality','Education_level','Citizenship',
                'Citizenship_number','Fathers_name','Mothers_name','Grandfathers_name','Name_of_institution',
                'location','Bank_ac_no','Bank_branch_name','Date_of_training']


class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields=['Form_number','Branch_name','client_license_code','Name','gender','photo','Temporary_Address','Permanent_address',
                'Contact_number','Email','password','Nationality','Education_level','Citizenship','Citizenship_number',
               'Company_name','Company_location','Income_source','Fathers_name','Mothers_name','Grandfathers_name' ]





