from django import forms
from .models import MyForm

# Create your forms here.
class MyFormForm(forms.ModelForm):
    class Meta:
        model = MyForm
        fields = '__all__'