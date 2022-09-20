from django.shortcuts import render

from recipes.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes.html", context)


def detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}
    return render(request, "detail.html", context)
