from django.shortcuts import render

# Create your views here.
from agent.forms import SigninForm


def signin(request):
    form=SigninForm
    return render(request,"agent/signin.html",{"form":form})



