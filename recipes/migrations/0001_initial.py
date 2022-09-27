# Generated by Django 4.1.1 on 2022-09-27 22:13

import uuid

import django.core.validators
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cooking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ingredients",
                    models.JSONField(
                        help_text="Ingredients of this recipe when available"
                    ),
                ),
                (
                    "difficulty",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                (
                    "instructions",
                    models.TextField(
                        help_text="Instructions of this recipe when available"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Nutrition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("kcal", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Quantity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        choices=[("g", "grams"), ("ml", "millilitres")],
                        help_text="Choose a unit (grams or millilitres)",
                        max_length=2,
                    ),
                ),
                (
                    "portion",
                    models.DecimalField(decimal_places=2, default=0, max_digits=50002),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unique ID for this particular recipe across whole database",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("author", models.CharField(blank=True, max_length=50)),
                ("short_description", models.CharField(blank=True, max_length=10000)),
                ("link", models.URLField(max_length=500)),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ["title", "rating"],
            },
        ),
        migrations.CreateModel(
            name="Serving",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("people", models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Time",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("preparation", models.DurationField()),
                ("cooking", models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name="Metadata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("add_date", models.DateTimeField(auto_now_add=True)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("notes", models.CharField(max_length=1000)),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
    ]
