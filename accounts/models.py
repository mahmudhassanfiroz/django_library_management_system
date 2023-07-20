from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    # Additional fields for user refistration
    # Add your custom fields here
    phone_number = models.CharField(max_length=15, blank=True)
