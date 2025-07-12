from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'category',
        'price',
        'is_available',
        'created_at',
    )
    search_fields = (
        'name',
        'description',
        'category',
        'location',
    )
    list_filter = (
        'category',
        'condition',
        'is_available',
        'created_at',
    )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'  # ✅ لتصفح حسب تاريخ الإضافة

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and not change:
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['owner']
        return super().get_readonly_fields(request, obj)
