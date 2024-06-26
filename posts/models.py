from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    MEAL_CHOICES =(
        ("breakfast", "breakfast"),
        ("lunch", "lunch"),
        ("dinner", "dinner"),
        ("appetizer", "appetizer"),
        ("dessert", "dessert"),
        ("snack", "snack"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_kk2xpx', blank=True
    )
    directions = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    meals = models.CharField(max_length=50, choices=MEAL_CHOICES, default='lunch')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.recipe_name}'
