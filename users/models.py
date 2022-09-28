from statistics import mode

from django import forms
from django.db import models
from location_field.forms.plain import PlainLocationField

# Create your models here.


class UserForm(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField
    email = models.EmailField(max_length=50)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    user_location = PlainLocationField(
        based_fields=[f"{models.CharField(max_length=50)}"]
    )
