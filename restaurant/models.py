from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title}: {str(self.price)}"
