from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CommentForm, CommentUpdateForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Recipe, Comment
from django.shortcuts import get_object_or_404


# Home view:
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

# About view:
def about (request):
    return render(request, 'about.html')

# Profile view:
@login_required
def profile(request):
    recipe = Recipe.objects.all()
    comment = Comment.objects.filter(user=request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)    
    context = {
        'recipes' : recipe,
        'comments' : comment,
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'profile.html',context)


# Recipe detail view:
@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    comments = recipe.comments.all()
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'comments':comments})

# Add comment
@login_required
def comment_add(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comment_form = CommentForm(request.POST or None)
    comment_form.instance.user = request.user
    if request.POST and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.recipe = recipe
        new_comment.save()
        return redirect('recipe_detail',recipe_id=recipe_id)
    else:
        comment_form = CommentForm()
    return render(request, 'comment/comment_add.html', {"comment_form" : comment_form})

# Edit comment
@login_required
def comment_edit(request, recipe_id, comment_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment_form = CommentUpdateForm(request.POST or None,instance=comment)
    if request.POST and comment_form.is_valid():
        comment_form.save()
        return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        comment_form = CommentUpdateForm()
    return render(request, 'comment/comment_edit.html', {"comment_form" : comment_form})

# Delete comment
@login_required
def comment_delete(request, recipe_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    recipe_id = comment.recipe.id
    if request.method == 'POST':
        comment.delete()
        return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        return render(request,'comment/comment_delete.html')

# Authentication view:
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