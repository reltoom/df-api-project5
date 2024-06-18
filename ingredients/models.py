from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
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
    )
    measurement = models.CharField(
        max_length=50,
        choices=MEASUREMENT_CHOICES,
        default="gram - g"
        )

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
