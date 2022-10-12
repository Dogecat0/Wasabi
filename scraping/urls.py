from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="scraping"),
    path("default_links", views.default_links, name="default_links"),
]
