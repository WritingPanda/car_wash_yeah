from django.contrib import admin
from .models import Service, Customer, Transaction


admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Transaction)
