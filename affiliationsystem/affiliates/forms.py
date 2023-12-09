
from django import forms
from .models import Sale

class SaleRecordForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'affiliate'] 
