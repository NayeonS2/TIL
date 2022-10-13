from django import forms
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)
        labels = {
            
            'risk': '투자 성향',
            'company': '관심 운용사',
            'period': '예상 투자 기간',
            'money': '예상 투자 금액',
        }

    