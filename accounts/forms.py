from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser


# ✅ نموذج تسجيل المستخدم الجديد
class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label="الاسم الكامل",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': "الاسم الكامل",
            'class': "form-control"
        })
    )

    phone_number = forms.CharField(
        label="رقم الجوال",
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'مثال: 0501234567',
            'pattern': r'^05\d{8}$',
            'title': 'رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام',
            'class': "form-control"
        })
    )

    email = forms.EmailField(
        label="البريد الإلكتروني",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com',
            'class': 'form-control'
        })
    )

    is_collector = forms.BooleanField(
        required=False,
        label="هل أنت مشتري؟",
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'phone_number', 'is_collector', 'password1', 'password2']
        labels = {
            'full_name': 'الاسم الكامل',
            'email': 'البريد الإلكتروني',
            'phone_number': 'رقم الجوال',
            'is_collector': 'هل أنت مشتري؟',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.startswith('05') or len(phone) != 10 or not phone.isdigit():
            raise forms.ValidationError("رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام صحيحة")
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("رقم الجوال مستخدم مسبقًا")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("البريد الإلكتروني مستخدم مسبقًا")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data.get('full_name')
        if commit:
            user.save()
        return user


# ✅ نموذج تسجيل الدخول
class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="البريد الإلكتروني",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(attrs={
            'placeholder': '********',
            'class': 'form-control'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("بيانات الدخول غير صحيحة")
            if not user.is_active:
                raise forms.ValidationError("هذا الحساب غير مفعل")
        return cleaned_data
