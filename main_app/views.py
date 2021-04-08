from django.shortcuts import render, redirect
from .models import Profile, Recipe


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def about (request):
    return render(request, 'about.html')

def profile (request):
    return render(request, 'profile.html')