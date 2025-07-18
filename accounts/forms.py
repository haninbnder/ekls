from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser

# 🔐 نموذج تسجيل المستخدم
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="البريد الإلكتروني",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'placeholder': "example@email.com",
            'class': "form-control"
        })
    )

    username = forms.CharField(
        label="اسم المستخدم",
        max_length=150,
        widget=forms.TextInput(attrs={
            'oninput': "checkUsernameAvailability(this.value);",
            'placeholder': "اسم المستخدم",
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

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone_number', 'is_collector', 'password1', 'password2']
        labels = {
            'email': 'البريد الإلكتروني',
            'username': 'اسم المستخدم',
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("اسم المستخدم غير متاح")
        return username


# 🔐 نموذج تسجيل الدخول باستخدام البريد الإلكتروني أو رقم الجوال أو اسم المستخدم
class UserLoginForm(forms.Form):
    identifier = forms.CharField(
        label="البريد الإلكتروني أو اسم المستخدم أو رقم الجوال",
        widget=forms.TextInput(attrs={
            'placeholder': "ادخل البريد الإلكتروني أو اسم المستخدم أو رقم الجوال",
            'class': "form-control"
        })
    )
    password = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(attrs={
            'placeholder': "كلمة المرور",
            'class': "form-control"
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('identifier')
        password = cleaned_data.get('password')

        if identifier and password:
            try:
                user = CustomUser.objects.get(phone_number=identifier)
                username = user.username
            except CustomUser.DoesNotExist:
                try:
                    user = CustomUser.objects.get(email=identifier)
                    username = user.username
                except CustomUser.DoesNotExist:
                    username = identifier  # اسم مستخدم كافتراضي

            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("بيانات الدخول غير صحيحة")
            self.user = user
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)
