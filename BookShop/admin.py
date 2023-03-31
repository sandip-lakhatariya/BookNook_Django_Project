from django.contrib import admin
from .models import Book, Contact, Order

# Register your models here.

admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(Order)