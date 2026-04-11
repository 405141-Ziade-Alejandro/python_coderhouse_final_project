from inventory.models import Supply
from django import forms

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'