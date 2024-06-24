from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_kk2xpx', blank=True
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.recipe_name}'


class Ingredient(models.Model):
    MEASUREMENT_CHOICES =(
    ("milliliter - ml", "milliliter - ml"),
    ("deciliter - dl", "deciliter - dl"),
    ("litre - l", "litre - l"),
    ("teaspoon - tsp", "teaspoon - tsp"),
    ("tablespoon - tbsp", "tablespoon - tbsp"),
    ("fluid ounce - fl oz", "fluid ounce - fl oz"),
    ("cup - c", "cup - c"),
    ("pint - pt", "pint - pt"),
    ("quart - qt", "quart - qt"),
    ("gallon - gal", "gallon - gal"),
    ("milligram - mg", "milligram - mg"),
    ("gram - g", "gram - g"),
    ("kilogram - kg", "kilogram - kg"),
    ("pound - lb", "pound - lb"),
    ("ounce - oz", "ounce - oz"),
    ('unit', 'units'),
    )

    post = models.ForeignKey('Post', related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    measurement = models.CharField(max_length=20, choices=MEASUREMENT_CHOICES)

    def __str__(self):
        return f'{self.quantity} {self.measurement} of {self.name}'