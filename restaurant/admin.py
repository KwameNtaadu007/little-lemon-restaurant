from django.contrib import admin
from .models import Booking 
from .models import Employee
from .models import Menu

# Register your models here.
admin.site.register(Booking)
admin.site.register(Employee)
admin.site.register(Menu)
