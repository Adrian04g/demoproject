from django.db import models

# Create your models here.
# Utilizando ModelForm
class MyForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    time_log = models.DateTimeField(help_text='Enter the date and time in the format: YYYY-MM-DD HH:MM:SS')