from django.db import models
from django.urls import reverse
# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    ctype=models.CharField(max_length=100)

    def get_absolute_url(self):  # new
        return reverse('CompanyDetailView', args=[str(self.pk)])

