from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    نموذج لإدخال أو تعديل بيانات منتج.
    يشمل: الاسم، الوصف، السعر، الفئة، الحالة، التوفر، وصورة المنتج.
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'condition', 'is_available', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل اسم المنتج'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل وصفًا واضحًا للمنتج',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'مثال: 1500'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'condition': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("يجب أن يكون اسم المنتج 3 أحرف على الأقل.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("السعر يجب أن يكون أكبر من الصفر.")
        return price
