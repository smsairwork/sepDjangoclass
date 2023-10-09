from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'index.html')


def add_products(request):
    return render(request, 'add-products.html')


def view_products(request):
    return render(request, 'view-products.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User creation success')
            return redirect('register-url')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html',{'form': form})
