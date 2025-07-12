# orders/forms.py

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """
    نموذج لإنشاء الطلب يتيح اختيار المنتج وتحديد الكمية.
    المستخدم يتم ربطه تلقائيًا في view ولا يظهر في الفورم.
    """
    class Meta:
        model = Order
        fields = ['product', 'quantity']  # المستخدم مرتبط تلقائيًا في view
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'required': True,
                'placeholder': 'أدخل الكمية المطلوبة'
            }),
        }
        labels = {
            'product': 'المنتج',
            'quantity': 'الكمية',
        }
