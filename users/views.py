from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
