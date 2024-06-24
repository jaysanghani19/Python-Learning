from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =[
            'title',
            'description',
            'price',
            'summary',
            'features'
        ]

class RawForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    summary = forms.CharField()
    features = forms.BooleanField(required=False)