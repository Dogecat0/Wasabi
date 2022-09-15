from django.db import models

# Create your models here.
class Recipes(models.Model):
    title = models.CharField(max_length=50)
    cooking_time = models.DecimalField(max_digits=3, decimal_places=1) # Cooking time normally is represented in hours(e.g 1.5h, 12h) or in minutes(e.g 50min)
    ingredients = models.TextField
    difficulty = models.PositiveSmallIntegerField
    instructions = models.TextField # How to cook in each step
