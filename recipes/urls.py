from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.recipe_index, name='recipe_index'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
]