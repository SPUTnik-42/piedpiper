from django.shortcuts import render, redirect
from .forms import RegisterForm 
from django.contrib import messages

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts/login")
        else:
            messages.error(response, "Please fill up the Signup form correctly")

    else:
        form = RegisterForm()
    return render(response, "signup.html", {"form":form})