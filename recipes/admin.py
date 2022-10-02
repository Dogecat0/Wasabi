from django.contrib import admin

from .models import Cooking, Nutrition, Recipe, Tags, Time

# Register your models here.

# Define the admin calss
# Register the Admin calss for Recipe using the decorator
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # fieldsets = ((None, {"fields": ("name", "author", "rating")}),)

    list_display = ("name", "author", "rating", "get_tags")

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    @admin.display(
        description="dietary restrictions and cuisine types",
    )
    def get_tags(self, obj):
        return ", ".join(o.name for o in obj.tags.dietary_and_cuisine.all())


admin.site.register(Nutrition)
admin.site.register(Cooking)
admin.site.register(Time)
admin.site.register(Tags)
