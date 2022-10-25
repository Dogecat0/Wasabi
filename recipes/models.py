import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns.
from django_measurement.models import MeasurementField
from measurement.measures import Mass
from taggit.managers import TaggableManager


# For Time, Cooking, Metadata, Nutrition and Tags, need to check again about 'recipe_name' and return self.recipe_name is the best way to representing objects.
class Time(models.Model):
    preparation = models.DurationField(help_text="Preparation time in HH:MM:SS format.")
    cooking = models.DurationField(help_text="Cooking time in HH:MM:SS format.")


class Cooking(models.Model):
    ingredients = models.JSONField(
        help_text="Ingredients of this recipe when available"
    )
    difficulty = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0
    )
    # How to cook in each step
    instructions = models.TextField(
        help_text="Instructions of this recipe when available"
    )


# TODO: Make 'scaping' app with Website(Link, Date) -> Response
# Plus Recipe-Scraper data mapping (this includes comments)


class Nutrition(models.Model):
    kcal = models.SmallIntegerField(default=0, blank=False)
    fat = MeasurementField(measurement=Mass)
    saturates = MeasurementField(measurement=Mass)
    carbohydrates = MeasurementField(measurement=Mass)
    sugars = MeasurementField(measurement=Mass)
    fibre = MeasurementField(measurement=Mass)
    protein = MeasurementField(measurement=Mass)
    salt = MeasurementField(measurement=Mass)


class DietaryTags(models.Model):
    dietary = TaggableManager(blank=True, help_text="Tags for dietary restrictions.")


class CuisineTags(models.Model):
    cuisine = TaggableManager(blank=True, help_text="Tags for cuisine types.")


class Recipe(models.Model):
    """Model representing a recipe."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular recipe across whole database",
    )
    photo = models.FileField(upload_to="photos", default="photos/missing.png")
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True)
    # It might be a list of images too
    # image = models.Field(path="/img", blank=True)
    short_description = models.CharField(max_length=10000, blank=True)
    link = models.URLField(
        max_length=500
    )  # need for further scraping and keeping track of website version
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0
    )
    serves = models.PositiveSmallIntegerField(default=1)
    cooking = models.OneToOneField(Cooking, on_delete=models.CASCADE, null=True)
    # ForeignKey used because one recipe only have one certain set of time informations,
    # but one set of time informations could match more than one recipes.
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE, null=True)
    dietary_tags = models.ForeignKey(DietaryTags, on_delete=models.CASCADE, null=True)
    cuisine_tags = models.ForeignKey(CuisineTags, on_delete=models.CASCADE, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    # Define the default ordering of records when querying model type.
    class Meta:
        ordering = ["name", "rating"]

    def __str__(self):
        """String for representing the Recipe object (in Admin site)."""
        return self.name

    def get_absolute_url(self):
        return reverse("recipe", args=[str(self.id)])
