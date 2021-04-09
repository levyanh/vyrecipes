
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Profile model:
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar')

    def __str__(self):
        return self.user.username

# Recipe model:   
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

# Comment model:
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    text = models.TextField(max_length=240)
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.user)
