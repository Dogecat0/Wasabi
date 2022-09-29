import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns.
from django_measurement.models import MeasurementField
from measurement.measures import Energy, Mass, Volume
from taggit.managers import TaggableManager


class Quantity(models.Model):
    UNIT = (("g", "grams"), ("ml", "millilitres"))
    # Upto 50kg
    unit = models.CharField(
        max_length=2,
        choices=UNIT,
        blank=False,
        help_text="Choose a unit (grams or millilitres)",
    )
    portion = models.DecimalField(
        default=0, blank=False, max_digits=50000 + 2, decimal_places=2
    )


class Serving(models.Model):
    people = models.PositiveSmallIntegerField(default=1)
    quantity = Quantity


class Time(models.Model):
    preparation = models.DurationField()
    cooking = models.DurationField()


class Cooking(models.Model):
    ingredients = models.JSONField(
        help_text="Ingredients of this recipe when available"
    )
    difficulty = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0
    )
    instructions = models.TextField(
        help_text="Instructions of this recipe when available"
    )  # How to cook in each step
    time = Time()


class Metadata(models.Model):
    # This includes dietary restrictions and cuisine types.
    # Data accuracy depends on scraping.
    tags = TaggableManager()
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=1000)


# TODO: Make 'scaping' app with Website(Link, Date) -> Response
# Plus Recipe-Scraper data mapping (this includes comments)


class Nutrition(models.Model):
    recipe_name = models.CharField(
        max_length=50, help_text="The name of the related recipe"
    )
    # FIXME: May need further update for 'kcal'
    # kcal = models.PositiveSmallIntegerField(default=0, blank=False)
    # fat = MeasurementField(measurement_class="Mass", unit_choices=(("g", "g")))
    # saturates = MeasurementField(measurement_class="Mass", unit_choices=(("g", "g")))
    # carbohydrates = MeasurementField(
    #     measurement_class="Mass", unit_choices=(("g", "g"))
    # )
    # sugars = MeasurementField(measurement_class="Mass", unit_choices=(("g", "g")))
    # fibre = MeasurementField(measurement_class="Mass", unit_choices=(("g", "g")))
    # protein = MeasurementField(measurement_class="Mass", unit_choices=(("g", "g")))
    # salt = MeasurementField(measurement_class="Mass", unit_choices=(("g", "g")))

    def __str___(self):
        "String for representing the Nutrition object"
        return self.recipe_name


class Recipe(models.Model):
    """Model representing a recipe."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular recipe across whole database",
    )
    title = models.CharField(max_length=50)
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
    serving = Serving()
    cooking = Cooking()
    # OnetoOneField used because one recipe only have one certain set of nutrition informations and vince versa.
    nutrition = models.ForeignKey(Nutrition, on_delete=models.SET_NULL, null=True)
    meta = Metadata()

    # Define the default ordering of records when querying model type.
    class Meta:
        ordering = ["title", "rating"]

    def __str__(self):
        """String for representing the Recipe object (in Admin site)."""
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
