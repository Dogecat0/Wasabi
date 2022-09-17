from django.shortcuts import render
from recipes.models import Recipes

# Create your views here.
def recipe_index(request):
    recipes = Recipes.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_index.html', context)

def recipe_detail(request, pk):
    recipe = Recipes.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)
