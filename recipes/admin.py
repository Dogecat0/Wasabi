from django.contrib import admin

from .models import Cooking, CuisineTags, DietaryTags, Nutrition, Recipe, Time

# Register your models here.

# Define the admin calss
# Register the Admin calss for Recipe using the decorator
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "author",
        "rating",
        "get_dietary_tags",
        "get_cuisine_tags",
        "get_difficulty",
        "get_preparation_time",
        "get_cooking_time",
    )

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .prefetch_related("dietary_tags", "cuisine_tags", "cooking", "time")
        )

    # Display dietary tags
    @admin.display(
        description="dietary restrictions",
    )
    def get_dietary_tags(self, obj):
        return ", ".join(o.name for o in obj.dietary_tags.dietary.all())

    # Display cuisine tags
    @admin.display(
        description="cuisine types",
    )
    def get_cuisine_tags(self, obj):
        return ", ".join(o.name for o in obj.cuisine_tags.cuisine.all())

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

    # Add list filter
    # TODO: Update the display of tags from tags object to actual values.
    list_filter = (
        "rating",
        "dietary_tags",
        "cuisine_tags",
        "time__cooking",
        "time__preparation",
        "cooking__difficulty",
    )


admin.site.register(Nutrition)
admin.site.register(Cooking)
admin.site.register(Time)
admin.site.register(DietaryTags)
admin.site.register(CuisineTags)
