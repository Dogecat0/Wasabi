from django.shortcuts import render
from django.views import generic

from recipes.models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RecipeListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        # Get the first 5 recipes from the database.
        return Recipe.objects.all()[:5]

    template_name = "recipes/list.html"


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/detail.html"


# def detail(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     context = {"recipe": recipe}
#     return render(request, "detail.html", context)
