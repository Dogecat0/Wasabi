from django.urls import path

from recipes import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-recipes", views.RecipeListView.as_view(), name="all-recipes"),
]
