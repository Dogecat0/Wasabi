# Generated by Django 4.1.1 on 2022-09-30 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cooking",
            name="recipe_name",
        ),
        migrations.RemoveField(
            model_name="metadata",
            name="recipe_name",
        ),
        migrations.RemoveField(
            model_name="nutrition",
            name="recipe_name",
        ),
        migrations.RemoveField(
            model_name="time",
            name="recipe_name",
        ),
    ]
