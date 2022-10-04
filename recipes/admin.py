from django.contrib import admin

from .models import Cooking, Nutrition, Recipe, Tags, Time

# Register your models here.

# Define the admin calss
# Register the Admin calss for Recipe using the decorator
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "author",
        "rating",
        "get_tags",
        "get_difficulty",
        "get_preparation_time",
        "get_cooking_time",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags", "cooking", "time")

    # Display tags
    @admin.display(
        description="dietary restrictions and cuisine types",
    )
    def get_tags(self, obj):
        return ", ".join(o.name for o in obj.tags.dietary_and_cuisine.all())

    # Display cooking.difficulty
    @admin.display(
        description="cooking difficulty (0-100)",
    )
    def get_difficulty(self, obj):
        return obj.cooking.difficulty

    # Display preparation time
    @admin.display(
        description="preparation time",
    )
    def get_preparation_time(self, obj):
        time: Time = obj.time
        return time.preparation

    # Display cooking time
    @admin.display(
        description="cooking time",
    )
    def get_cooking_time(self, obj):
        time: Time = obj.time
        return time.cooking


admin.site.register(Nutrition)
admin.site.register(Cooking)
admin.site.register(Time)
admin.site.register(Tags)
