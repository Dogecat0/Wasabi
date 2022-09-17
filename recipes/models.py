from django.db import models

# Create your models here.
class Recipes(models.Model):
    title = models.CharField(max_length=50)
    cooking_time = models.CharField(max_length=10) # Cooking time normally is represented in hours(e.g 1.5h, 12h) or in minutes(e.g 50min)
    ingredients = models.TextField(default='ingredients displayed of this recipe when it is available')
    difficulty = models.PositiveSmallIntegerField(default=1)
    instructions = models.TextField(default='instructions displayed of this recipe when it is available') # How to cook in each step
