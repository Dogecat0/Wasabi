from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from taggit.managers import TaggableManager


class Quantity(models.Model):
    GRAMS = "grams"
    MILLILITRES = "millilitres"
    unit = ((GRAMS, "g"), (MILLILITRES, "ml"))
    # Upto 50kg
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
        verbose_name="Ingredients of this recipe when available"
    )
    difficulty = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0
    )
    instructions = models.TextField(
        verbose_name="Instructions of this recipe when available"
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

# FIXME: Find better representation for below:
class Nutrition(models.Model):
    kcal = models.PositiveIntegerField(default=0, blank=False)
    fat = Quantity()
    saturates = Quantity()
    carbohydrates = Quantity()
    sugars = Quantity()
    fibre = Quantity()
    protein = Quantity()
    salt = Quantity()


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
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
    nutrition = Nutrition()
    meta = Metadata()
