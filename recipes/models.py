import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns.
from django_measurement.models import MeasurementField
from measurement.measures import Energy, Mass, Volume
from taggit.managers import TaggableManager


# For Time, Cooking, Metadata and Nutrition, need to check again about 'recipe_name' and return self.recipe_name is the best way to representing objects.
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


class Metadata(models.Model):
    # This includes dietary restrictions and cuisine types.
    # Data accuracy depends on scraping.
    tags = TaggableManager(help_text="Tags for dietary restrictions and cuisine types.")
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=1000, help_text="Extra notes about the recipe.")


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


class Recipe(models.Model):
    """Model representing a recipe."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular recipe across whole database",
    )
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
    cooking = models.OneToOneField(Cooking, on_delete=models.SET_NULL, null=True)
    time = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True)
    # ForeignKey used because one recipe only have one certain set of nutrition informations,
    # but one set of nutrition informations could match more than one recipes.
    nutrition = models.ForeignKey(Nutrition, on_delete=models.SET_NULL, null=True)
    meta = models.OneToOneField(Metadata, on_delete=models.SET_NULL, null=True)

    # Define the default ordering of records when querying model type.
    class Meta:
        ordering = ["name", "rating"]

    def __str__(self):
        """String for representing the Recipe object (in Admin site)."""
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
