from django.urls import path

from recipes import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.RecipeListView.as_view(), name="all_recipes"),
    path("<str:pk>", views.RecipeDetailView.as_view(), name="recipe"),
]
