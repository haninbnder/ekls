from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    نموذج لإضافة أو تعديل منتج.
    يحتوي على الحقول: الاسم، الوصف، السعر، الفئة، الصورة.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ادخل اسم المنتج'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'ادخل وصفاً للمنتج',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ادخل السعر'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
