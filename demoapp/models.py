from django.db import models

# Create your models here.
# Ejemplo de reservacion
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
# ejemplo de reservacion
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.customer.name} on {self.date} at {self.time}"