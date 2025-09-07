from django.db import models

# Create your models here.

# Utilizando ModelForm
class MyForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    time_log = models.DateTimeField(help_text='Enter the date and time in the format: YYYY-MM-DD HH:MM:SS')

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

