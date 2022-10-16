from django.urls import path

from recipes import views

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipes"),
    path("<str:pk>/", views.RecipeDetailView.as_view(), name="recipe"),
]
