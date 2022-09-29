from django.contrib import admin

from .models import Nutrition, Recipe

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Nutrition)
