from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),              # عرض جميع الطلبات الخاصة بالمستخدم
    path('create/', views.order_create, name='order_create'),   # إنشاء طلب جديد
    path('<int:pk>/', views.order_detail, name='order_detail'), # عرض تفاصيل الطلب
]
