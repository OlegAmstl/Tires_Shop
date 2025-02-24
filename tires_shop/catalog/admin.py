from django.contrib import admin

from .models import Brand, Tire


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'diameter', 'width', 'height', 'season', 'price', 'stock', 'image']
    list_filter = ['brand', 'season']
    search_fields = ['name', 'brand__name']
    readonly_fields = ['image']

