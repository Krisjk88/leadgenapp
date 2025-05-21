from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name