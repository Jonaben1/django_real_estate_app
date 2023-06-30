from django.db import models
from datetime import datetime

# Create your models here.

class Listing(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    n_bedrooms = models.IntegerField(null=True)
    n_bathrooms = models.IntegerField(null=True)
    sqft = models.IntegerField()
    image = models.ImageField(upload_to='images')
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name








class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    submitted_on = models.DateTimeField(default=datetime.now)
    message = models.TextField()

    def __str__(self):
        return self.name


