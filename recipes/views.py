from multiprocessing import context

import genericpath
from django.shortcuts import render
from django.views import generic

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


class RecipeListView(generic.ListView):
    model = Recipe

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RecipeListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["some_data"] = "This is just some random data"
        return context

    def get_queryset(self):
        return Recipe.objects.all()[:5]

    template_name = "recipes/recipe_list.html"


# def detail(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     context = {"recipe": recipe}
#     return render(request, "detail.html", context)
