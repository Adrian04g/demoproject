from django.contrib import admin
<<<<<<< HEAD
from .models import MyForm

# Register your models here.
admin.site.register(MyForm)
=======
from .models import Customer,Reservation
# Register your models here.

admin.site.register(Customer)
admin.site.register(Reservation)
>>>>>>> 1e278e88ee8e8527d8eecf55460631878dc1ba0e
