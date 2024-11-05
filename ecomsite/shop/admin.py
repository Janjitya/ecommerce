from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "e-Shop"
admin.site.index_title = "Manage e-Shop"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Set Default Category'
    list_display = ('title','price','discount_price','category','description',)
    search_fields = ('title','category')
    actions = ('change_category_to_default',)
    fields = ('title','price','discount_price','description',)
    list_editable = ('price','discount_price','description')

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
