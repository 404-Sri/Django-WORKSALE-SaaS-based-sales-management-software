from django.contrib import admin

# Register your models here.

from . models import registration_table,contact_table,add_customer_table

admin.site.register(registration_table)
admin.site.register(contact_table)
admin.site.register(add_customer_table)
