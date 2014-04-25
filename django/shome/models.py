from django.db import models

# Create your models here.
class UniversityInfo(models.Model):
    name         = models.CharField(max_length=500)
    url	         = models.CharField(max_length=500)
    introduction = models.CharField(max_length=500)
    ranking      = models.CharField(max_length=500)
    studentnum   = models.CharField(max_length=500)
    fee          = models.CharField(max_length=500)
    image        = models.CharField(max_length=500)
    apartment    = models.CharField(max_length=500)
    food         = models.CharField(max_length=500)
    housing      = models.CharField(max_length=500)
    car          = models.CharField(max_length=500)
    translink    = models.CharField(max_length=500)
    shopping     = models.CharField(max_length=500)
    tourist      = models.CharField(max_length=500)
    sports       = models.CharField(max_length=500)
    googlemaps   = models.CharField(max_length=500)