from django.shortcuts import render
from recipes.models import Recipe

# Create your views here.
def recipe_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_index.html', context)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)
