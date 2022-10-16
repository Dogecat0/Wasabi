from django.shortcuts import render
from recipes.models import CuisineTags, DietaryTags, Recipe

# Create your views here.


def index(request):
    """View function for recipes main page of the site"""
    num_recipes = Recipe.objects.all().count()
    num_cuisines = CuisineTags.cuisine.all().distinct().count()
    num_dietary_restrictions = DietaryTags.dietary.all().distinct().count()
    context = {
        "num_recipes": num_recipes,
        "num_cuisines": num_cuisines,
        "num_dietary_restrictions": num_dietary_restrictions,
    }
    return render(request, "index.html", context=context)
