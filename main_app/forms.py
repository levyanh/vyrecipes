from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']