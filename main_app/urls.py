from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('recipes/', views.home, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('recipes/<int:recipe_id>/comment/', views.comment_add, name="comment_add"),
    path('recipes/<int:recipe_id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('recipes/<int:recipe_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]