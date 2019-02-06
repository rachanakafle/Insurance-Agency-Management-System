from django.shortcuts import render

# Create your views here.
from account.forms import SigninForm, SignupForm


def signin(request):
    form = SigninForm()
    return render(request, "account/signin.html", {"form": form})

def signup(request):
    form = SignupForm()
    return render(request, "account/signup.html", {"form": form})




def base(request):
    return render(request,"account/base.html")

def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("account:signin")


