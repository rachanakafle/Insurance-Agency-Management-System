from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


from CMS.forms import SignupForm, SigninForm, AgentForm, ClientForm


def signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "User created successfully")
        else:

            messages.info(req, "Invalid form")
    else:

        form = SignupForm()
    return render(req,"CMS/signup.html",{"form":form})


def signin(req):
    if req.method == "POST":
        form = SigninForm(req.POST)
        username = form["username"].value()
        password = form["password"].value()
        user = authenticate(req, username=username,  password=password)
        if User is not None:
            login(req, user)
            messages.success(req, "Successfully logged in")
            return redirect("CMS:base")
        else:
            messages.error(req, "Invalid Username or Password")
    else:
        form = SigninForm
    return render(req, "CMS/signin.html", {"form":form})

@login_required(login_url='/signin')
def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("CMS:signin")


def base(request):
    return render(request,"CMS/base.html")

def agent(request):
    if request.method=='POST':
        form=AgentForm(request.POST,request.FILES or None)
        if form.is_valid():
            value=form.save(commit=False)
            value.user_id=request.user.id
            value.save()
            messages.success(request,'Registered successfully')
            return redirect("CMS:signup")
    else:
        form=AgentForm()
    return render(request,'CMS/agentregister.html',{"form":form})

def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES or None)
        if form.is_valid():
            value = form.save(commit=False)
            value.user_id = request.user.id
            value.save()
            messages.success(request, 'client created successfully')
            return redirect("CMS:signup")
    else:
        form =ClientForm ()
    return render(request, 'CMS/clientregister.html', {"form": form})










