from django.db import models


class AbstractProfile(models.Model):
    """abstract class to profile user"""
    dni = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)
    cell_phone = models.CharField(max_length=15)

    class Meta:
        abstract = True
