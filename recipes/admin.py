from django.contrib import admin

from .models import Cooking, Metadata, Nutrition, Recipe, Time

# Register your models here.

# Define the admin calss
# Register the Admin calss for Recipe using the decorator
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # fieldsets = ((None, {"fields": ("name", "author", "rating")}),)

    list_display = ("name", "author", "rating")


admin.site.register(Nutrition)
admin.site.register(Cooking)
admin.site.register(Time)
admin.site.register(Metadata)
