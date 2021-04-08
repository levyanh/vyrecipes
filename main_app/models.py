
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.jpg',upload_to='user_avatar')

    def __str__(self):
        return self.user.username
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="recipe_images")
    ingredient = models.TextField(max_length=2000)
    instruction = models.TextField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_date']