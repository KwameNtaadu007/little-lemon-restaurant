from django.db import models


# Create your models here.
class Booking(models.Model):
        first_name = models.CharField(max_length = 200)
        last_name = models.CharField(max_length = 200)
        guest_count = models.IntegerField()
        reservation_time = models.DateField(auto_now=True)
        comments = models.CharField(max_length=1000)


# Create Employee models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name
    

# Create your menu models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000,default='')

    def __str__(self):
        return self.name