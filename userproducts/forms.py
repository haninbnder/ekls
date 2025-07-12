from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'type', 'price', 'weight', 'image']
        labels = {
            'name': '📛 اسم المنتج:',
            'description': '📝 وصف المنتج:',
            'type': '📦 نوع المنتج:',
            'price': '💰 السعر (ريال):',
            'weight': '⚖️ الوزن (كجم):',
            'image': '📷 صورة المنتج:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
