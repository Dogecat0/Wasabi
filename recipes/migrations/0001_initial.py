# Generated by Django 4.1.1 on 2022-10-05 10:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_measurement.models
import measurement.measures.mass
import taggit.managers
import uuid


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
            name="CuisineTags",
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
                    "cuisine",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="Tags for cuisine types.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DietaryTags",
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
                    "dietary",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="Tags for dietary restrictions.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
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
                ("kcal", models.SmallIntegerField(default=0)),
                (
                    "fat",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
                (
                    "saturates",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
                (
                    "carbohydrates",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
                (
                    "sugars",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
                (
                    "fibre",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
                (
                    "protein",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
                (
                    "salt",
                    django_measurement.models.MeasurementField(
                        measurement=measurement.measures.mass.Mass
                    ),
                ),
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
                (
                    "preparation",
                    models.DurationField(
                        help_text="Preparation time in HH:MM:SS format."
                    ),
                ),
                (
                    "cooking",
                    models.DurationField(help_text="Cooking time in HH:MM:SS format."),
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
                ("name", models.CharField(max_length=50)),
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
                ("serves", models.PositiveSmallIntegerField(default=1)),
                ("add_date", models.DateTimeField(auto_now_add=True)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                (
                    "cooking",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.cooking",
                    ),
                ),
                (
                    "cuisine_tags",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.cuisinetags",
                    ),
                ),
                (
                    "dietary_tags",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.dietarytags",
                    ),
                ),
                (
                    "nutrition",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.nutrition",
                    ),
                ),
                (
                    "time",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.time",
                    ),
                ),
            ],
            options={
                "ordering": ["name", "rating"],
            },
        ),
    ]
