from django.shortcuts import render

# Create your views here.
from client.forms import SigninForm


def signin(request):
    form=SigninForm
    return render(request,"client/signin.html",{"form":form})
