from django.contrib import admin
from .models import Menu, Booking  # Import the Menu and Booking models

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
