from django.db import models

# Create your models here.

class Rides(models.Model):
    rider=models.CharField(max_length=150)
    driver=models.CharField(max_length=150)
    pickup_location=models.CharField(max_length=110)
    dropoff_location = models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_at=models.CharField(max_length=100)
    updated_at=models.CharField(max_length=100)
