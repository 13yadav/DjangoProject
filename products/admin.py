from django.contrib import admin
from products.models import Phone, Laptop, Feedback


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('ph_id', 'brand_name', 'model', 'number_in_stock', 'price')
    list_filter = ('brand_name',)
    exclude = ('date_added',)


class LaptopAdmin(admin.ModelAdmin):
    list_display = ('lap_id', 'brand_name', 'model',
                    'number_in_stock', 'price')
    list_filter = ('brand_name',)
    exclude = ('date_added',)


admin.site.site_header = 'Showroom Management'
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Feedback)
