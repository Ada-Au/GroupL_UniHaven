from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    isSpecialist = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}: {self.isSpecialist and "Specialist" or "Member"}'

class PropertyOwner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.EmailField()
    def __str__(self):
        return self.name

class Accommodation(models.Model): # Do we need a name for the accommodation? For editing and view
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50) # should this be enum?
    availablePeriodStart = models.DateField()
    availablePeriodEnd = models.DateField()
    bed = models.IntegerField()
    bedroom = models.IntegerField()
    price = models.FloatField()
    address = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)
    rating = models.FloatField(blank=True, null=True)
    owner = models.ForeignKey(PropertyOwner, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.type} ({self.address})'

class Reservations(models.Model): # What happens when multiple member make a reservation for the same accommodation?
    id = models.AutoField(primary_key=True)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, limit_choices_to={'isAvailable': True})
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member',limit_choices_to={'isSpecialist': False}) # should specialist be able to rent a room too?
    specialist = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='specialist', blank=True, null=True, limit_choices_to={'isSpecialist': True})
    isConfirmed = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    rating = models.FloatField(blank=True, null=True)
    def __str__(self):
        return f'{self.accommodation.type} by {self.member.name}'