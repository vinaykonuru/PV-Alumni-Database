from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class AlumniProf(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grad_year = models.IntegerField(max_digits=4,decimal_places=0)
    college = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.IntegerField(max_digits=5, decimal_places=0)
    job = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    hs_activities = models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now_add=True)