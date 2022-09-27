from django import forms
from .models import Proveedor,Product

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = '__all__'