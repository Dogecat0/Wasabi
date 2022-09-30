from django.contrib import admin

from .models import Cooking, Metadata, Nutrition, Recipe, Time

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Nutrition)
admin.site.register(Cooking)
admin.site.register(Time)
admin.site.register(Metadata)
