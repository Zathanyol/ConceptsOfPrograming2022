from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def createUser(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Howdy doody!")
            return redirect("inside")


    context = {"form": form}
    return render(request, "loginService/register.html", context)


def login(request):

    if request.user.is_authenticated:
        return redirect("inside")

    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password =request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "loginService/login.html", context)


def inside(request):
    return render(request, "loginService/inside.html")

def userLogout(request):
    logout(request)
    return render(request, "loginService/login.html")