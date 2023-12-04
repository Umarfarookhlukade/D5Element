from django.db import models

# Create your models here.

class therepy(models.Model):
    p_name = models.CharField(max_length=200, null=False , blank=False)
    address = models.CharField(max_length=200)
    phone  = models.CharField(max_length=25, null=False , blank=False)
    treatment = models.CharField(max_length=200, null=False , blank=False)
    fees = models.CharField(max_length=100)
    date = models.DateField()
    nextdate = models.DateField()