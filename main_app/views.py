from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Profile, Recipe


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def about (request):
    return render(request, 'about.html')

def profile (request, user_id):
    profiles = Profile.objects.get(user_id=user_id)
    print(profiles,"!!!!!!")
    for each in Profile.objects.all():
        print(each.avatar)
    return render(request, 'profile.html', {'profiles': profiles})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})