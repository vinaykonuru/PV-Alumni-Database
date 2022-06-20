from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class AlumniProf(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grad_year = models.CharField(max_length=4, blank=True, null=True)
    college = models.CharField(max_length=200, blank=True, null=True)
    major = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    employer = models.CharField(max_length=100, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    hs_activities = models.CharField(max_length=100, blank=True, null=True)
    newsletter = models.BooleanField(default=True)
    interview = models.BooleanField(default=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user',null=True)
