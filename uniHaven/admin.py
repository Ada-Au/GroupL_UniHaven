from django.contrib import admin
from .models import *
class UserFilter(admin.ModelAdmin):
    list_filter = [
        "isSpecialist"
    ]

class AccommodationFilter(admin.ModelAdmin):
    list_filter = [
        "isAvailable"
    ]

admin.site.register(User, UserFilter)
admin.site.register(PropertyOwner)
admin.site.register(Accommodation, AccommodationFilter)
admin.site.register(Reservations)

