from django.contrib import admin
from .models import menu
from .models import custumer
from .models import deliveryMan


class menuAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name','price')

class custumerAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name','lat_long','address','email')

class deliveryManAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name','lat_long')

admin.site.register(menu, menuAdmin)
admin.site.register(custumer, custumerAdmin)
admin.site.register(deliveryMan, deliveryManAdmin)