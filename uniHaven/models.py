from django.db import models

class User(models.Model):  # For specialist, member
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class PropertyOwner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50) # email? phone number?

class Accommodation(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    availablePeriodStart = models.DateField()
    availablePeriodEnd = models.DateField()
    bed = models.IntegerField()
    bedroom = models.IntegerField()
    price = models.FloatField()
    address = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)
    owner = models.ForeignKey(PropertyOwner, on_delete=models.CASCADE)