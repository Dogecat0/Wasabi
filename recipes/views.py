from django.shortcuts import render

from recipes.models import CuisineTags, DietaryTags, Recipe


def index(request):
    """View function for home page of the site"""
    num_recipes = Recipe.objects.all().count()
    # TODO: To update the count of numbers of cuisines and dietary restriction types from Tags
    num_cuisines = CuisineTags.cuisine.all().distinct().count()
    num_dietary_restrictions = DietaryTags.dietary.all().distinct().count()
    context = {
        "num_recipes": num_recipes,
        "num_cuisines": num_cuisines,
        "num_dietary_restrictions": num_dietary_restrictions,
    }
    return render(request, "index.html", context=context)


# def detail(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     context = {"recipe": recipe}
#     return render(request, "detail.html", context)
